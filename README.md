# SecondBrain
Inspired by [LDP](https://youtu.be/XTwDhiDGk50?si=-96yj4ElEUdxGF_n), this is an obsidian vault I use to manage my tasks and goals. The vault's structure and plugins used has certain underlying philosophies, which I will lay down in this document.
## Vault Structure
The vault has the following top level folders:
- `Lists/`: For keeping misc lists such as Topics to explore (`Explore.md`), Misc reading list (`Reading.md`), etc.
- `Work/`: For housing my *projects* and *disciplines*.

Each **Discipline** and **Project** contains the following components. These components (except for the `README.md`) are kept inside a `/(Discipline | Project)/Dive` folder.
- `Milestones`
- `Reading`
- `References`
- `Tasks`
- `Roadmap`(Optional)
- `Scratch/`(Optional): For keeping random notes.
- `README.md`: The MOC or dashboard for the project/discipline. The 
- Disciplines have an optional `Pillars.md`. Pillars are tenets that guide the discipline.

```
├── Dashboard.md
├── Inbox
├── Lists
│   ├── Entertainment.md
│   ├── Explore.md
│   ├── Reading.md
│   ├── Resolutions.md
│   └── TasksNext.md
├── README.md
└── Work
    ├── D-discipline1
    │   ├── Dive
    │   │   ├── Milestones.md
    │   │   ├── Pillars.md
    │   │   ├── Reading.md
    │   │   ├── References.md
    │   │   └── Tasks.md
    │   └── README.md
    ├── D-discipline2
    │   ├── Dive
    │   │   ├── Milestones.md
    │   │   ├── Pillars.md
    │   │   ├── Reading.md
    │   │   ├── References.md
    │   │   ├── Roadmap.md
    │   │   ├── Scratch
    │   │   │   ├── _INDEX.md
    │   │   │   ├── 'GPT 5 advice on wind mills.md'
    │   │   │   └── 'What is a Wind Mill.md'
    │   │   └── Tasks.md
    │   └── README.md
    ├── P-project1
    │   ├── Dive
    │   │   ├── Milestones.md
    │   │   ├── Reading.md
    │   │   ├── References.md
    │   │   ├── Scratch
    │   │   └── Tasks.md
    │   └── README.md
    └── P-project2
        ├── Dive
        │   ├── Milestones.md
        │   ├── Reading.md
        │   ├── References.md
        │   ├── Scratch
        │   │   ├── 'ChatGPT discussion on.md'
        │   │   └── Scratch.md
        │   └── Tasks.md
        └── README.md
```
# Quick Glossary
- `Dive`: A folder for 'diving into' the main content. 