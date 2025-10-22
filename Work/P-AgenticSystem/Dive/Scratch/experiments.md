What experiments can we do ?

---
- Once we have a mechanism in place that can judge the plan, use the misc and wants and improve the plans and execution, we can do an ablation study that measures the impacts of those things.
- Latency, token cost, tool-call count
- Other papers are doing ablation studies.
- Adversarial prompting (check [[system_desc]])
- How many planning steps it takes to get a good plan according to our likert scales.

---
Each component agent has the following degrees of freedom
1. The query itself
2. Role
3. Constraints
4. Data
5. Additional context (Planner gets RAG extracted info
6. Memory (Executor)

- We can do a study of how strictly the executor adheres to the planner's plan. 
- Benchmark the system on HLE's healthscience related questions and our in house dataset.
- Make comparisons with off the shelf LLMs and previous agentic architectures.