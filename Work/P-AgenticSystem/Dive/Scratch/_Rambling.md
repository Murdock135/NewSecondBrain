- Brainstorm how to handle comments within NORS
- QA dataset
	- We could automatically generate a QA dataset using the available data
	- pass@k- The agent can satisfactorily handle a question when k of its responses to that question are good.
	- Using self-consistency decoding
- Ramblings about time series
	- A smoothed time period e.g. a monthly progression would be better?
	- Model the temperature
	- Think about the occurence of salmonella as a process (Salmonella inception -> Salmonella observation)
- Is it possible to infer location of contamination?
- Can we get outputs in terms of probabilities?
- How can we impute missing data?
- Maybe we can use LllamaIndex/Llamaparse to
	- Clean and Merge datasets.
	- add the data documentations.
- Provide a list of URLs the LLM should scrape when trying to answer a question.
- Find all APIs for datasets.
- Need to discuss how to incorporate data on same thing e.g. poultry sampling, but for different time periods. For example 2013 will be different from 2014.
- Build a knowledge graph
	- Build a knowledge graph that links entities like county's economic profile with salmonella rates and encodes data like correlations, causal hypothesis.
	- Incorporate ontologies and domain-specific taxonomies to ensure that relationships are semantically meaningful and can be interpreted universally. (Recommendation by gpt o3 mini)
	- By fusing datasets into a semantic network, the system creates a unified representation that reveals hidden relationships. The knowledge graph paves the way for advanced querying (e.g., using SPARQL) and allows for richer insights through the exploitation of network structures and connectivity
- On providing info about data
	- Unless we use a bug model, we should do it manually because if we iterate over the datasets and provide df.head(), the datasets which are excel files would quickly consume the context window. 
- Using langgraph
	- We don't need to add messages to a node unless its the executor because the executor needs to use its own previous executions. 
	- A candidate structure for the state object
```python
	class State(TypedDict):
		query: str
		plan: Plan # create 'Plan' object before
		results: List[StateMessage]
```
- Add the system prompts and llms in the [runtime configuration](https://langchain-ai.github.io/langgraph/how-tos/graph-api/#add-runtime-configuration).
```python
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnableConfig
from langgraph.graph import MessagesState
from langgraph.graph import END, StateGraph, START
from typing_extensions import TypedDict


class ConfigSchema(TypedDict):
    model: str


MODELS = {
    "anthropic": init_chat_model("anthropic:claude-3-5-haiku-latest"),
    "openai": init_chat_model("openai:gpt-4.1-mini"),
}


def call_model(state: MessagesState, config: RunnableConfig):
    model = config["configurable"].get("model", "anthropic")
    model = MODELS[model]
    response = model.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(MessagesState, config_schema=ConfigSchema)
builder.add_node("model", call_model)
builder.add_edge(START, "model")
builder.add_edge("model", END)

graph = builder.compile()

# Usage
input_message = {"role": "user", "content": "hi"}
# With no configuration, uses default (Anthropic)
response_1 = graph.invoke({"messages": [input_message]})["messages"][-1]
# Or, can set OpenAI
config = {"configurable": {"model": "openai"}}
response_2 = graph.invoke({"messages": [input_message]}, config=config)["messages"][-1]

print(response_1.response_metadata["model_name"])
print(response_2.response_metadata["model_name"])
```
- Parallelise certain computations e.g. retrieval from various sources.
	- https://youtu.be/l7lvoiCvcVU?si=TBzufVs9xmojL0Kx
- Store data context as separate vector stores, which the language models will access based on need.
- https://youtu.be/WL7V9JUy2sE?si=4baP6-DUWSgUU0Hr
- Give the Executor the docs for huggingface.

---

- Adjust the df loading function as per this chat:
  Excellent question. This gets to the core of how agent tool execution and state management work.

The short answer is: **Yes, the agent will be able to access `df` in subsequent tool calls, but this design has significant drawbacks.**

Let's break down why it works and why it's a potentially fragile pattern.

### How it Works: The `global` Keyword

1.  **Shared Execution Environment:** When an agent uses tools, those tools are typically executed within the same, single Python process. This process has its own memory and global scope.

2.  **The `global df` Statement:** This is the key. When your `load_dataset` function is called, the line `global df` tells the Python interpreter: "The `df` variable I am about to assign to is not a new variable local to this function. It is the `df` variable that exists in the global scope of this entire script/process."

3.  **State Persistence:** Because the DataFrame is assigned to a *global* variable, it persists in the Python process's memory after the `load_dataset` function has finished executing.

### The Agent's Workflow

Here is how the agent would interact with this and another potential tool (like a Python REPL):

1.  **User Request:** "Load the data from `my_data.csv` and show me the first 5 rows."

2.  **Tool Call 1: `load_dataset`**
    *   The agent determines it needs to load the data first.
    *   It calls your tool: `load_dataset(file_path='my_data.csv')`.
    *   Your function executes, creating the DataFrame and storing it in the **global** variable `df`.
    *   The function returns the *string*: `"Loaded dataset into variable `df`.\n\nPreview"`.

3.  **Agent's Reasoning:**
    *   The agent sees the successful return message. The message explicitly tells it that the data is now in a variable named `df`.

4.  **Tool Call 2: A different tool (e.g., a `python_repl` tool)**
    *   To fulfill the second part of the request ("show me the first 5 rows"), the agent now generates code that uses the `df` variable.
    *   It might call a `python_repl` tool with the code: `print(df.head())`.
    *   This new tool call executes in the **same Python process**. Since `df` exists in the global scope, this code runs successfully and returns the head of the DataFrame.

5.  **Final Answer:** The agent uses the output from the second tool call to give the user the final answer.

### The Problems with this Global State Approach

While this works for simple cases, it's considered a fragile design for several reasons:

1.  **Name Collisions:** What happens if the user wants to load a second dataset? `load_dataset('other_data.csv')` would simply **overwrite** the global `df` variable. The first dataset would be lost. There is no way to work with two dataframes at once.
2.  **Hidden State:** The fact that `df` is available is a "side effect" of the `load_dataset` tool. It's not explicitly passed between tools. This makes the agent's logic harder to trace and debug. The dependency is implicit and "magical."
3.  **Lack of Scalability:** This pattern fails in any concurrent or multi-user environment. If two users made requests at the same time in the same process, they would be fighting over the single global `df`.
4.  **Error Prone:** If another tool accidentally modifies or deletes the global `df`, it could break the entire chain of thought for the agent.

### A More Robust Alternative: Using Handles/Identifiers

A much better and more common pattern is to avoid global state and instead manage state explicitly, returning a "handle" or "ID" to the agent.

Here's how you could rewrite your tools:

```python
import pandas as pd
import uuid

# This dictionary will act as our in-memory store for dataframes.
# It is still a global variable, but it's a structured manager, not a single-use variable.
dataframe_store = {}

@tool
def load_dataset_pro(file_path, sheet_name=None):
    """
    Loads a dataset and returns a unique ID to access it later.
    Args:
        file_path (str): Path to the dataset file.
        sheet_name (str, optional): Name of the Excel sheet to load.
    Returns:
        str: A message containing the unique ID for the loaded dataframe.
    """
    if file_path.endswith('.csv'):
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            return f"PythonError: {e}"
    elif file_path.endswith('.xlsx') and sheet_name:
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        except Exception as e:
            return f"PythonError: {e}"
    else:
        raise ValueError("Unsupported file format or missing sheet name for Excel file.")
    
    # Generate a unique ID for this dataframe
    df_id = f"df_{uuid.uuid4().hex[:6]}"
    
    # Store the dataframe in our manager dictionary
    dataframe_store[df_id] = df
    
    return f"Successfully loaded dataset. Use the ID `{df_id}` to refer to it in other tools."

@tool
def get_dataframe_head(df_id: str, n: int = 5):
    """
    Returns the first n rows of a loaded dataframe using its ID.
    Args:
        df_id (str): The unique ID of the dataframe, given by `load_dataset_pro`.
        n (int): The number of rows to display.
    """
    if df_id not in dataframe_store:
        return f"Error: Dataframe with ID '{df_id}' not found."
    
    return dataframe_store[df_id].head(n)
```

**How the improved workflow looks:**

1.  **Agent calls:** `load_dataset_pro('my_data.csv')`
2.  **Tool returns:** `"Successfully loaded dataset. Use the ID `df_a1b2c3` to refer to it in other tools."`
3.  **Agent now knows** it needs to use the ID `df_a1b2c3`.
4.  **Agent calls:** `get_dataframe_head(df_id='df_a1b2c3', n=5)`
5.  **Tool returns:** The actual head of the DataFrame, which the agent can then show to the user.

This approach allows the agent to manage multiple dataframes, makes dependencies explicit, and is far more robust.

---
- The datasets cannot be set by the planner in the Plan object because then, the executor doesn't have autonomy in case it wants to analyze a different dataset. We need a way to dynamically change the plan with each iteration of the executor.
- How to evaluate the system
	- Create a dataset like that in [AgentRewardBench](https://arxiv.org/pdf/2504.08942)
	- We then let the system run again such that it follows the expert annotations. Then we use semantic similarity or some other measure to check how different the initial generation is (from the regeneration)
	- We can then use RLHF to make the system more like an epidemiologist.
	- What if we use Alvey's protoforms and then use Dempster Shafer Theory to study assumptions (read below)
- Ask the system to produce a list of possible assumptions, rank ordered. We should probe the system to obtain a quantified 'amount' of belief in those assumptions.
---
- We can use the `wants` and/or `misc` to signal that there is more to be done to complete the current step. Then we can invoke a helper `llm` that does this.