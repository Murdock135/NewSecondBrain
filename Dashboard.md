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
	- Course- [Nand2Tetris](https://www.coursera.org/learn/build-a-computer/home/module/1)
		- Next Lesson- Unit 1.4: Hardware Description Language
	- Course- Computer Networks
- Athletics
	- Basic workout (3 d/w)
	- Football (2 d/w)
- Books
```apb

Crime and Punishment: 100/100
Analysis I (Terence Tao): 12/550
Man's Search For Meaning (Viktor Frankl): 120/138
Stylish Academic Writing (Helen Sword): 8/182
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
