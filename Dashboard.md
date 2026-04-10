# Your Next Tasks
```tasks
path includes Lists/TasksNext.md
not done
```

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
Man's Search For Meaning (Viktor Frankl): 138/138
Stylish Academic Writing (Helen Sword): 27/182
Brave New World (Aldous Huxley): 44/258
Hands-on Large Language Models (Jay Alamar): 16/425
```


---
# Lists
![[Untitled 1.base]]

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
tag includes #task
```
