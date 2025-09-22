# Your Next Tasks
```tasks
path includes Lists/TasksNext.md
```

# Ongoing Projects
- Academic
	- Research on LLMs: (1) Epistemology on LLMs (2) Combining Evidence
	- Course- [Nand2Tetris](https://www.coursera.org/learn/build-a-computer/home/module/1)
	- Course- Principles of Programming Languages
- Sports
	- Tennis
	- Football
- Books
	- Crime and Punishment



---
# Lists
[[Lists/Reading|Reading]]
[[Resolutions]]
[[Explore]]
[[Entertainment]]
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
