# Repository Guidelines

> This repository is an Obsidian vault (NewSecondBrain). Keep changes tidy, reversible, and link‑safe.

## Project Structure & Module Organization
- Root notes: `Dashboard.md`, ad‑hoc notes in `Inbox/`.
- Lists: checklists and indexes in `Lists/`.
- Work: active domains and projects under `Work/` (e.g., `D-discipline1/`, `P-project2/`).
- Obsidian config lives in `.obsidian/` (do not hand‑edit unless you know the setting).

## Build, Test, and Development Commands
- Search notes: `rg -n "pattern"` or `rg -n "\[\[.*\]\]"` for wiki links.
- Find stale indexes: `find Work -type f -iname "*index*"`.
- Preview before destructive actions and exclude `.git/` (example):
  - `find . -path ./.git -prune -o -type f -iname "*index*" -print`

## Coding Style & Naming Conventions
- Filenames: Title Case, concise (e.g., `Project Charter.md`). Avoid leading underscores.
- Folders: prefix type + dash (e.g., `P-projectName`, `D-disciplineName`).
- Headings: start with a single `#` title; use sentence‑case headings below.
- Links: prefer Obsidian wikilinks `[[Note Name]]`; keep names stable to avoid link rot.
- Tags: keep to a small, curated set (e.g., `#inbox`, `#waiting`).

## Testing Guidelines
- Link sanity: after renames, search for `[[Old Name]]` via `rg` and update.
- Orphans: list notes with few backlinks and review their placement.
- Optional: keep lightweight “verification” notes inside `Lists/` (what changed, why).

## Commit & Pull Request Guidelines
- Commit format: `content(scope): summary` (e.g., `content(work/p-project2): add scratch log`).
  - Types: `content`, `refactor`, `structure`, `meta`.
- One topic per commit; include examples or paths touched.
- PRs: brief description, rationale, and impact on links or structure. Reference related notes/paths.

## Security & Configuration Tips
- Do not commit secrets. Treat `.obsidian/` as local config; avoid editing `workspace.json` in PRs.
- Always preview mass changes; never operate in `.git/`.
