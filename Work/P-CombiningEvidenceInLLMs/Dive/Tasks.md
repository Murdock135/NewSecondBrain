
- [ ] #task Explore Abstract Meaning Representation graphs and Semantic Role Labelling (SRL)
- [x] #task Create an output schema for the UoD extractor ✅ 2026-08-21
- [x] #task Create an output schema for the Frame of Discernment extractor. ✅ 2026-08-21
- [ ] #task In the system prompt of the data generator, introduce another concept- a matrix that indicates which models have been given a piece of information $\lambda$ by the human. Each row represents the 'existence' vector for a piece of evidence. For example $\lambda=(1,0,1)^T$ means evidence $\lambda$ has been given to model 1 and 3 but not 0. This will be produced by the LLM in the data sample.
- [x] #task Implement a factory pattern for the components (*extractor, data_generator, bpa_assigner, etc*) by having a function `configure` ✅ 2026-08-21
	- [x] #task the base class should indicate the `configure` contract ✅ 2026-08-21
	- [ ] #task the component should implement `configure`
- [x] #task Use the google-genai idiomatic way of setting system prompts, inference properties e.g. top-p, temp. see https://googleapis.github.io/python-genai/#system-instructions-and-other-configs ✅ 2026-08-21

# Archived

- [x] #task Come up with possible frames of discernments, write about it and meet Dr. A to brainstorm ✅ 2025-11-06 🔒 [[2025-11-30]] 🕸️ Tasks
- [x] #task Create Project structure ✅ 2025-11-10 🔒 [[2025-11-30]] 🕸️ Tasks
- [x] #task Create the project structure, the registry pattern, one SDK integration ✅ 2025-11-30 🔒 [[2025-11-30]] 🕸️ Tasks
	- [x] #read Python tutorial on classes (2 hours) ✅ 2025-11-30
	- [ ] #read 
- [x] #task code the first hypothesis extractor ✅ 2025-11-30 🔒 [[2025-11-30]] 🕸️ Tasks
- [x] #task Build a synthetic data generator that uses an LLM to create the dataset. This would allow us to control the amount of conflict that each model will have. For example, perhaps M1 and M2 align and together contradict with M3. ✅ 2026-02-11 🔒 [[2026-02-12]] 🕸️ Tasks
- [x] #task Rewrite the system prompt ✅ 2026-02-12 🔒 [[2026-02-12]] 🕸️ Tasks
