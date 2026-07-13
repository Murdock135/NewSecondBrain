# 🚀 Project SPARQ Task List



## Ideas
1. Incorporate a way to detect possible overlaps within the sub-steps of the steps of each plan. Perhaps have a critic for the planner.
2. Use deliverables. Each Step should have deliverables. The deliverables can be used by the planner (when it's thinking) to better decide dependent steps. Furthermore, this will help the executor agent decide on completion criteria.
3. Track token count going into the worker agents and then implement smart ways of handling.



## 🏗️ Infrastructure & DevOps
- [ ] #task Fix **Dockerfile** and bash script that runs docker

## 🤖 Model & Provider Logic
- [ ] #task Every time **SPARQ** runs, get list of bedrock models and cache it. If list updates, replace old list with newer one.
- [ ] #task Give the executor the full plan and the data context.
- [ ] #task Build **guardrails** - OpenAI moderation API
- [ ] #task Set up **CLI args**
	- [ ] #task Pick output location
	- [ ] #task Pick LLM provider and model
	- [ ] #task Make verbose or not

## 🛠️ Tool Integration & Agents
- [ ] #task Create a **writer node** that will write the final answer nicely
- [ ] #task Create the **weather calling tool**
- [ ] #task Give the aggregator file reading tool so it can read everything the executor outputted.

## 📊 Data & Testing
- [ ] #task **Import tests**
	- [ ] #task Learn to use **Ruff** and `pkgutils`
		- [ ] #task Write the import tests file
- [ ] #task Run one question 5 times
- [ ] #task Fix the `df` summary extraction code for `census_population` data
- [ ] #task Create a script to extract raw **poultry sampling data**
- [ ] #task Create a **likert scale**

## 📖 Research & Documentation
- [ ] #task Read **Langgraph's changelog** [Link](https://docs.langchain.com/oss/python/releases/changelog)
- [ ] #task Read [Techniques for monitoring LLMs on AWS](https://aws.amazon.com/blogs/machine-learning/techniques-and-approaches-for-monitoring-large-language-models-on-aws/)
- [ ] #task Read literature Mitesh sent out
- [ ] #read [Think aloud protocol book](https://pure.uva.nl/ws/files/716505/149552_Think_aloud_method.pdf)
- [ ] #task Listen to recording of meeting with **Dr. A.**
- [ ] #task Include an **example run** in the methods section
- [ ] #task Write **READMEs** for the datasets on HuggingFace #discuss
- [ ] #task Create a doc with **issues/requests/ramblings** #planned

# Comments
1) Public/general knowledge, 2) Scientist/epidemiology/government, 3) Outreach to populations (extension, community health workers), 4) from poultry industry
2) Try using deep-coder https://docs.langchain.com/oss/python/deepagents/code/overview#full-list-of-built-in-tools

# Archived

- [x] #task use an if name == main #planned ✅ 2025-03-19 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task put data used for research (proof of concept inside a separate dir) #planned ✅ 2025-03-20 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Put the data documentations in a folder from which the llm can extract information. #ongoing ✅ 2025-03-20 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Fix the paths pointing to the data so that they are generic enough to be reproducible #planned(5m) ✅ 2025-03-21 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task incorporate ollama with langchain ✅ 2025-03-21 🔒 [[2025-06-20]] 🕸️ tasks
	- [x] #task read langchain-ollama (30m) #ongoing ✅ 2025-03-21
- [x] #task Read Python's 'Input and Output' tutorial #ongoing ✅ 2025-03-21 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Parse the output from the llm #ongoing ✅ 2025-03-22 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Use ChatPromptTemplate to format the message so that it is explicit as to what is the human message #planned ✅ 2025-03-29 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Extract the json plan #ongoing ✅ 2025-04-07 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task get structured output ✅ 2025-04-24 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Make powerpoint ✅ 2025-05-05 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Create a function in config.py that will create output directories stamped by time #ongoing ✅ 2025-05-05 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task move utility functions to utils.py #planned ✅ 2025-05-06 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task create a explorer ✅ 2025-05-08 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task add {df_heads} to the planner's system message #planned ✅ 2025-05-08 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task make the `pipeline` func with planner, executor #ongoing ✅ 2025-05-14 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Create schematic of langchain system. ✅ 2025-05-14 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Read about FAISS ✅ 2025-05-14 🔒 [[2025-06-20]] 🕸️ tasks
	- [x] #task Read the Github wiki ✅ 2025-05-14
	- [x] #task Read the Github README.md ✅ 2025-03-17
- [x] #task create a router node that determines if the planner needs to be invoked or if it can answer the user's query itself. #ongoing ✅ 2025-05-25 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Add a loop (max 5 times) to force proper output schema ✅ 2025-06-02 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task create a script to download data ✅ 2025-06-04 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task create tools to access blob and list the files #ongoing ✅ 2025-06-04 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Change the system prompts to include text from manifest.json instead of tree #planned ✅ 2025-06-06 🔒 [[2025-06-20]] 🕸️ tasks
	- [x] #task dispose of get_tree_bash (put into archive) and create another function to read in `manifest.json` #planned ✅ 2025-06-06
- [x] #task migrate to langgraph #ongoing ✅ 2025-06-10 🔒 [[2025-06-20]] 🕸️ tasks
	- [x] #task planner ✅ 2025-05-25
	- [x] #task executor ✅ 2025-06-09
- [x] #task make the aggregator ✅ 2025-06-13 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task refine project structure #ongoing ✅ 2025-06-13 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task instead of invoking a new API call, add to the list of messages/ use memory. #planned ✅ 2025-06-13 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task Get gemini API and use it #ongoing ✅ 2025-06-18 🔒 [[2025-06-20]] 🕸️ tasks
- [x] #task put test queries into config.toml #planned ✅ 2025-06-24 🔒 [[2025-06-24]] 🕸️ tasks
- [x] #task path to manifest should be set in Config #planned ✅ 2025-06-24 🔒 [[2025-06-27]] 🕸️ tasks
- [x] #task Write a routine to check whether the data mentioned in the manifest actually exists #planned ✅ 2025-06-24 🔒 [[2025-06-27]] 🕸️ tasks
- [x] #task Create json for QA dataset #ongoing 🔒 [[2025-06-27]] 🕸️ tasks
- [x] #task Create video on baseline system 🔒 [[2025-06-27]] 🕸️ tasks
- [x] #task Create a function to run the agentic system on a list of questions #planned 🔒 [[2025-06-27]] 🕸️ tasks
- [x] #task path to manifest should be set in Config #planned ✅ 2025-06-24 🔒 [[2025-07-18]] 🕸️ tasks
- [x] #task Write a routine to check whether the data mentioned in the manifest actually exists #planned ✅ 2025-06-24 🔒 [[2025-07-18]] 🕸️ tasks
- [x] #task Finish report #ongoing 🔒 [[2025-07-18]] 🕸️ tasks
- [x] #task Create json for QA dataset #ongoing 🔒 [[2025-07-18]] 🕸️ tasks 
- [x] #task Create a script to run every expert query #ongoing ✅ 2025-07-23 🔒 [[2025-08-08]] 🕸️ tasks
- [x] #task Study Likert scale #ongoing 🔒 [[2025-08-08]] 🕸️ tasks
- [x] #task Write a README for the project  🔒 [[2025-08-08]] 🕸️ tasks
- [x] #task email Dr. Anand #planned 🔒 [[2025-09-23]] 🕸️ Tasks
- [x] #task The structured output generator isn't working well. It is not filling in the `code` field within the output schema. This may be because the code field generated by the LM is too lengthy. ✅ 2025-09-23 🔒 [[2025-09-23]] 🕸️ Tasks
- [x] #task Create function to save final answer #planned  🔒 [[2025-09-23]] 🕸️ Tasks
- [x] #task write an example .env file ✅ 2025-09-23 🔒 [[2025-09-26]] 🕸️ Tasks
- [x] #task docker build script should abruptly exit if .env and/or .secrets/.llm_apis isn't found ✅ 2025-09-25 🔒 [[2025-09-26]] 🕸️ Tasks
- [x] #task Write the quarterly report ✅ 2025-09-26 🔒 [[2025-09-26]] 🕸️ Tasks
- [x] #task create docker image #ongoing ✅ 2025-09-26 🔒 [[2025-09-26]] 🕸️ Tasks
	- [x] #task create `.dockerignore` #ongoing ✅ 2025-09-16
	- [x] #task create named volume for outputs ✅ 2025-09-26
	- [x] #task create named volume for secrets1 ✅ 2025-09-26
- [x] #task There is an issue with how we're handling `.venv/`. After the docker build creates a `.venv/` for the user, we are currently mounting the whole `PWD`  with `-v` and after the container is stopped (and even removed) the `.venv/` stays and the result is the following: ✅ 2025-09-28 🔒 [[2025-10-03]] 🕸️ Tasks
- [x] #task Docker build script should ask whether the user has already downloaded the data. If not, it should create a docker volume, change the HF_HOME, download the data and then start the project ✅ 2025-09-28 🔒 [[2025-10-03]] 🕸️ Tasks
- [x] #task Send the system names to team #planned ✅ 2025-09-28 🔒 [[2025-10-03]] 🕸️ Tasks
- [x] #task Rewrite README ✅ 2025-09-29 🔒 [[2025-10-03]] 🕸️ Tasks
- [x] #task Write abstract ✅ 2025-10-06 🔒 [[2025-10-14]] 🕸️ Tasks
- [x] #task Think about experiments ✅ 2025-10-07 🔒 [[2025-10-14]] 🕸️ Tasks
- [x] #task Calculate/estimate compute needed ✅ 2025-10-07 🔒 [[2025-10-14]] 🕸️ Tasks
	- [x] LLM calls API ✅ 2025-07-29
- [x] #task Create diagrams ✅ 2025-11-04 🔒 [[2025-11-04]] 🕸️ Tasks
	- [x] #task Architecture ✅ 2025-11-04
- [x] #task Make the diagram more detailed. Depict the information the planner has access to. ✅ 2025-12-02 🔒 [[2025-12-15]] 🕸️ Tasks
- [x] #task Create a custom python repl ✅ 2025-12-15 🔒 [[2025-12-15]] 🕸️ Tasks
	- Refs:
		- https://docs.python.org/3/library/code.html#module-code
- [x] #task Plan how to restructure ✅ 2025-12-15 🔒 [[2025-12-15]] 🕸️ Tasks
- [x] Restructuring ✅ 2026-01-19 🔒 [[2026-01-19]] 🕸️ Tasks
	- [x] #task Restructuring: Use a more robust method to set paths so that it works platform agnosticly (on windows, config should live in `%APPDATA%`) ✅ 2026-01-19
- [x] #task Restructure project ✅ 2026-01-19 🔒 [[2026-01-19]] 🕸️ Tasks
- [x] #task Create a custom python repl ✅ 2026-01-19 🔒 [[2026-01-19]] 🕸️ Tasks
	- Refs:
		- https://docs.python.org/3/library/code.html#module-code
		- Create new branch
		- Create new tool script `execute_code.py`
		- Create test script
		- After testing, use in `nodes/executor.py`
- [x] #task Make an AGENTS.md file ✅ 2026-02-03 🔒 [[2026-02-03]] 🕸️ Tasks
	- [x] #task Read Karpathy's tweet #next ✅ 2026-02-03
	- [x] #task Read claude code author's tweet #next ✅ 2026-02-03
- [x] #task fix USER_CONFIG_DIR in macos. Settings will use this to determine location for `.env` ✅ 2026-02-09 🔒 [[2026-02-09]] 🕸️ Tasks
- [x] #task Fix: If the code wants to import multiple *uninstalled packages*, it doesn't work because of the current implementation. Fix this. ✅ 2026-02-09 🔒 [[2026-02-09]] 🕸️ Tasks
- [x] #task Feature: Handle graphics/file operations when agent uses python_repl_tool ✅ 2026-02-09 🔒 [[2026-02-10]] 🕸️ Tasks
- [x] #task In the executor node, remove the checkpointer and manually append conversation state. This will ✅ 2026-03-10 🔒 [[2026-03-17]] 🕸️ 🚀 Project SPARQ Task List > 🤖 Model & Provider Logic
- [x] #task Remove timeout option from python_repl_tool. Set it to 1000s by default ✅ 2026-03-10 🔒 [[2026-03-17]] 🕸️ 🚀 Project SPARQ Task List > 🤖 Model & Provider Logic
- [x] #task Change how namespace is handled. Currently the namespace gradually accumulates over time. Use the following approach ✅ 2026-03-17 🔒 [[2026-03-17]] 🕸️ 🚀 Project SPARQ Task List > 🤖 Model & Provider Logic
- [x] #task Write test for new namespace handling logic ✅ 2026-03-17 🔒 [[2026-03-17]] 🕸️ 🚀 Project SPARQ Task List > 🤖 Model & Provider Logic
- [x] #task Read and understand namespace handling approach (3 hours ish) ✅ 2026-03-17 🔒 [[2026-03-17]] 🕸️ 🚀 Project SPARQ Task List > 🤖 Model & Provider Logic
- [x] #task Set up **AWS integration** ✅ 2026-04-14 🔒 [[2026-05-25]] 🕸️ 🚀 Project SPARQ Task List > 🏗️ Infrastructure & DevOps
	- [x] #task Place to set region (us-east-1 in `config.toml`) ✅ 2026-03-02
		- [x] #task Set `AWS_PROFILE` (sensd) ✅ 2026-03-02
- [x] #task Create a timeline for the Book Chapter #next ✅ 2026-04-15 🔒 [[2026-05-25]] 🕸️ 🚀 Project SPARQ Task List > 📖 Research & Documentation
- [x] #task Recursive building of config.toml (project root config -> user provided config) ✅ 2026-05-25 🔒 [[2026-05-25]] 🕸️ 🚀 Project SPARQ Task List > 🏗️ Infrastructure & DevOps
- [x] #task Create a `.env.example` so that example code doesn't have to be hardcoded in `settings.py` ✅ 2026-05-25 🔒 [[2026-05-25]] 🕸️ 🚀 Project SPARQ Task List > 🏗️ Infrastructure & DevOps
- [x] #task Use df_summaries_short in planner and executor system prompt ✅ 2026-05-25 🔒 [[2026-05-25]] 🕸️ 🚀 Project SPARQ Task List > 🤖 Model & Provider Logic
	- Refactor list
	- [x] system prompts ✅ 2026-05-25
	- [x] planner node module ✅ 2026-05-25
	- [x] executor node module ✅ 2026-05-25
	- [x] path to data summaries in `config.toml` ✅ 2026-05-25
