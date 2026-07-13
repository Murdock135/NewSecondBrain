- [ ] #task Use ToT (tree of thought) prompting with planner and ask it to produce multiple plans so that different plans can be implemented e.g. a non-linear regressor + linear regressor and can be parallelized.
- [ ] #task Add node `postprocess_results`. It's job is to create indexes of figures in `figures/` , tables in `tables/` , an `index.md`, `key_notes.md` (from the *executor node's* `execution_results` field)
- [ ] #task Introduce LSP features into the python repl so that worker agent can communicate with LSP and avoid *simple* errors instead of fix errors afterward
- [ ] #task Track token counts everywhere and implement **context engineering** (truncation, summarization, etc)
## optional
- [ ] #task Fix DevOps stuff
	- [ ] #task fix dockerfile
	- [ ] #task fix run scripts
- [ ] #task Implement lazy-updating bedrock model list and cross-checking with config files.

# Future work (v2)
- [ ] #task Planner supervisor
	- [ ] #task Basic plan review loop
- [ ] Executor supervisor
	- [ ] #task 
- [ ] #task Weather calling tool