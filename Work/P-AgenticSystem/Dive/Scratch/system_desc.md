This note explains the whole system

---
# TLDR
The agentic system can be described by the following graph:
`router -> planner -> executor -> aggregator -> formatter -> saver`

---
# Fix list
1. Only the planner's `step-description` is given to the executor. The executor
2. The executor's `wants` and `misc` are not used. 
3. We can add an ask the router to produce a `complexity : [0,1]` that assesses the complexity of the answer and then use the returned number to route to either the planner. We will have more understanding of what *it* thinks is a complex answer. 
	1. We should test the router's consistency- Whether it produces the same complexity for a given input, over many runs.
	2. Incorporate a 'complexity analysis' method in the future.
	3. Do F1 score analysis to test its accuracy in classifying the complexity.
4. Perform adversarial prompting to
	1. Check if it conflating correlation with causation.
	2. Other soundness checks.
	This may be best done using another 'adversarial' LLM that dynamically generates these prompts based on the current user query and final aggregated output.

---
# Description of the system
This agentic system, henceforth called SPARQ, is a simple system that is composed of the following agents.
1. A router
2. A planner
3. An executor
4. An aggregator
5. A formatter
6. A saver.
The key nodes are the planner, executor, aggregator and formatter. The router merely routes to the planner if the user's query qualifies as a complex query and the saver simply saves the trace of the system aka logs everything. If the query is not sufficiently complex, the router returns an output itself.

## Planner
The planner is burdened with the task of producing a plan. To ensure it generates a good plan, the following information is injected into its system prompt (these are currently fixed and cannot be changed by the user)
1. The data manifest
2. The summaries for the data (which includes (TODO: ))
3. The output schema it should follow.
The datasets - the summaries for which are injected - cannot be changed.
## Executor
The executor receives the planners output and tries to execute the plan using tools that it is equipped with. It does this by iterating over the steps within the plan. 
The executor is provided information about what's been done before and can only look at the current step. It cannot revisit previous steps or make any changes to the plan produced by the planner. After executing each step, it reports the following
1. A textual representation of the code it's written.
2. The results of the code it wrote.
3. Files it generated
4. Assumptions it made.
5. What it wants to execute the step in a better way.
6. Anything miscellaneous.
Note that while it does disclose its results, assumptions, wants and misc information, these aren't used anywhere else in the system and simply stored for provenance.

## Aggregator
The aggregator simply writes a report based on the executor's results.

# Evaluating the system
- Testing the system on Popular QA datasets like WikiTQ, TableBench, etc.1
- A dataset of questions has been created, comprised of questions sent by various health experts. Answers will be obtained for those questions and sent to the experts to be graded on a likert scale. Voluntary annotations from the experts will also be accepted.
- Do a sweep study wherein you shall study 'how good a language model do you need to make the system do well'. Use Bedrock models to do this since you have API credits.
- Check how many computational steps the planner plans to do. Each computational step is a step like 'finding correlation',  'building a regression model', etc.
# Notes
Currently, this system is only being applied in pathogen dynamics analysis; specifically salmonella. It will be used in a larger health-professional facing DSS system. 
