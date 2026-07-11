# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **NewSecondBrain**, an Obsidian vault used as a personal knowledge/task management system (inspired by "LDP" — see README.md). It is not a software project: there is no build, lint, or test suite. Changes here are edits to Markdown notes, and the main risks are broken wikilinks and inconsistent structure, not compile/runtime errors.

## Vault structure

- `Dashboard.md` — home page; links to `Lists/TasksNext.md` and runs Dataview/Tasks queries over `Work/`.
- `Lists/` — miscellaneous flat lists: `Explore.md`, `Reading.md`, `Entertainment.md`, `Resolutions.md`, `TasksNext.md`, `Scratch.md`.
- `Work/` — all **Disciplines** and **Projects**. Folder names are prefixed by kind:
  - `D-<Name>` = Discipline (an ongoing area, e.g. `D-AIAndComputing`, `D-HolisticDev`)
  - `P-<Name>` = Project (a bounded effort, e.g. `P-AgenticSystem`, `P-LinuxRice`)
- `copilot/` — data for the Obsidian Copilot plugin (`copilot-conversations/`, `copilot-custom-prompts/`).
- `.obsidian/` — Obsidian app config; mostly gitignored except `plugins/`, `themes/`, and a handful of top-level JSON config files (see `.gitignore`). Don't hand-edit `workspace.json`-type local state.
- `.scripts/make_work_item.py` — scaffolds a new Discipline/Project (see below).

### Anatomy of a Discipline/Project

Each item under `Work/` has:
- `README.md` at its root — the MOC/dashboard for that item, with YAML frontmatter:
  ```yaml
  ---
  name: <Display Name>
  kind:
    - Project        # or Discipline
  type:
    - Professional    # or Personal (Projects only; Disciplines usually omit `type`)
  ---
  ```
  followed by a row of wikilinks to its `Dive/` sub-pages (e.g. `Tasks`, `Milestones`, `References`, `Reading`).
- `Dive/` folder containing the substantive sub-pages: `Milestones.md`, `Reading.md`, `References.md`, `Tasks.md`, and optionally `Roadmap.md`, `Pillars.md` (Disciplines only), `Scratch/` (freeform notes), `Logs/` (dated entries), `attachments/` (images).
- `Scratch/` folders, when present, are indexed manually via an `_INDEX.md` inside them — hardlink every note you add there so the Index Checker plugin can verify nothing is orphaned.

The `Dashboard.md` Dataview query (`FROM "Work" WHERE file.name = "README"`) depends on every Discipline/Project README having a `README.md` filename with `name`/`kind`/`type` frontmatter — keep new items consistent with this or they won't show up. (Note: `P-LLMsInScientificMethod` and `P-LMErrorAnalysis` currently use `Readme.md` — inconsistent casing is a known rough edge, not something to silently "fix" mid-task.)

## Common commands

There's no build/test tooling; the useful commands are search and scaffolding.

```bash
# Search note content
rg -n "pattern"

# Find all wikilinks (e.g. before/after a rename, to catch link rot)
rg -n "\[\[.*\]\]"

# Find stale/duplicate index files
find Work -type f -iname "*index*"

# Preview file operations before anything destructive, excluding .git/
find . -path ./.git -prune -o -type f -iname "*index*" -print

# Scaffold a new Discipline or Project (creates Work/<Name>/README.md + Dive/{Milestones,Reading,References,Tasks,Roadmap}.md)
python .scripts/make_work_item.py
# then prompts for a name like "P-NewProject" or "D-NewDiscipline"
```

Note: `make_work_item.py` always creates a `Roadmap.md` even though not every existing item has one, and it never writes frontmatter into the new `README.md` (that function is a no-op stub) — fill in `name`/`kind`/`type` by hand after scaffolding.

## Conventions

- **Filenames**: Title Case, concise (e.g. `Project Charter.md`). No leading underscores except for manual indexes (`_INDEX.md`).
- **Folder prefixes**: `P-` for Projects, `D-` for Disciplines, followed by a CamelCase or spaced name.
- **Headings**: single `#` title at the top of a note; sentence-case for headings below that.
- **Links**: use Obsidian wikilinks `[[Note Name]]` (with `|display text` aliases as needed), not Markdown links, to stay in Obsidian's link graph. Keep note names stable — renames cause link rot that must be grepped and fixed (`rg -n "\[\[Old Name"`).
- **Tags**: small curated set, e.g. `#task`, `#next`, `#milestone`, `#inbox`, `#waiting`. Tasks use the `obsidian-tasks-plugin` syntax (`- [ ] #task ...`, done items get `✅ YYYY-MM-DD`).
- **Commits**: `content(scope): summary`, e.g. `content(work/p-project2): add scratch log`. Types in use: `content`, `refactor`, `structure`, `meta`. One topic per commit.

## Working safely

- Never operate inside `.git/`; never hand-edit `.obsidian/workspace.json`.
- Before any rename or delete that could affect links, search for references first (`rg -n "\[\[<Name>"`) and update all backlinks.
- Preview mass/glob changes (e.g. with `find ... -print`) before applying them.
- Don't commit secrets; there shouldn't be any in vault content, but check pasted content (e.g. `copilot/copilot-conversations/`) before committing.
