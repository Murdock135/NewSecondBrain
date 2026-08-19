# Your Next Tasks
Go to [[TasksNext]]

# Ongoing Projects
- Academic
	- Research on LLMs: (1) 
		1. Agentic System for pathogen analysis
		2. Combining Evidence
		3. Code diff analysis
		4. Socket Programming
	- Course- Computer Networks
- Athletics
	- Basic workout (3 d/w)
	- Football (2 d/w)
- Books
```apb

Analysis I (Terence Tao): 12/550
Stylish Academic Writing (Helen Sword): 27/182
Glimpses of world history (Jawaharlal Nehru): 1/972
```


---
# Projects

```dataview
TABLE
name AS "Name", kind AS "Kind", type AS "Type"
FROM "Work"
WHERE file.name = "README"
SORT kind ASC, type ASC, name ASC
```

# Project Milestones
```dataview
task from "Work"
where contains(tags, "#milestone") and !completed
```
# All tasks
```tasks
not done
```
