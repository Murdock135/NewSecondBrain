Several improvements to the system could be made
1. Adjusting the planner as more and more information is revealed during the execution of the plan. This will increase token expenditure.
2. The entire schema can be given to the aggregator, from which it can write a report.
3. A `synthesizer` node can process the aggregator's report and synthesize a concise answer. 
4. The system has more information about the data and will have done deeper analysis than the users. It is in a much better position to ask deeper research questions that help answer the user's original question. While it is true that the planner implicitly does this, asking the LLM to generate a 'plan' may be different from asking it to generate 'sub-research' questions. This will require making plans for each of the sub-research questions.
> 10-8-2025

- Can we introduce a goal tree to improve observability? Do we need to? Langgraph itself is a goal tree. We can increase the granularity of the tree.
- Token budgeting: How do we do this?
- Sub-research questions
- Hypothesis generation and falsification like POPPER.