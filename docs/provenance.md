# Provenance

This page records how the description was checked. It is not part of the product story on the front page.

Public pages do not name the upstream product or organization. The engine repository keeps that identity in its own upstream note. The source repository is private.

## Revisions

| Anchor | Commit | Date | What it is |
|---|---|---|---|
| First orchestrator commit in the source checkout | `9eb5bad` | 1 September 2026, 02:18 +03 | Start of the orchestrator history used below |
| Extraction base | `b6d72af5f9500486b8136bf6c24925d6558a5ccb` | 21 October 2026, 01:11 +03 | Recorded base in the engine upstream note. Present in the source checkout and an ancestor of its `main` |
| Published Fleet engine | `0e1693d` | 22 October 2026, 05:28 +03 | Engine revision these pages describe |
| Source `main` at review time | `5312a9ae5e0243d277111840050088dfd739b72a` | 23 October 2026, 01:56 +03 | Later than the extraction. Not claimed as part of Fleet |

The source checkout reviewed here was branch `main` at `5312a9ae`. The engine note still says the last sync is empty, which matches the commits on the orchestrator tree after `b6d72af`.

## What was counted

Counts below are only for readers who want the scope. They are not a measure of quality.

On source `main` at `5312a9ae`:

- 535 commits on that `main`. This is the development history of the delivery orchestrator that was abstracted into Fleet. It includes the work done before Fleet had its own repository. It is not the Git history of the published engine repository.
- 354 commits touch the `orchestrator/` tree. That figure is a narrower path filter, not a replacement for the 535. It leaves out documentation, tests, rules, scripts, and integration work that belong to the same development history.
- 347 of those path-filtered commits are contained in the extraction base `b6d72af`.
- 7 touch `orchestrator/` after that base. They are not in the published Fleet tree. Source work after the extraction is not presented here as already present in the published engine.

The path-filter command was `git rev-list --count <rev> -- orchestrator` in that checkout. Renames inside that tree are included by git's history simplification for the path. The first commit on the path is the initial delivery snapshot of 1 September 2026, not a later rename. The 535 count is `git rev-list --count 5312a9ae` on that same `main`, with no path filter.

## Authorship

Fleet was developed by Yunus Emre Cebe. Every commit that touches `orchestrator/` in that history uses that name. No other human author appears.

## What moved, and what was added

The extraction step copies the orchestrator into the Fleet package and renames the internal `sdlc` paths. That move is how the engine got its own repository. It is not the description of the work.

Already in use before the extraction:

- Architect specs and task lists from module analysis
- A planner with lane workers, worktrees, and pull requests
- Dependency waiting between tasks
- QA and Security prompts built from the diff and task results
- Quality gates, Slack questions, and spec approval

Added in the published Fleet engine, through `0e1693d`:

- A product-neutral workspace and profile, with product-specific settings moved to a pack
- Crash-safe atomic state, locks, and quarantine of corrupt interaction files
- Jira as a second input: filtered task and bug intake, story and epic analysis, sub-tasks, leases, and a comment channel
- Suspend and resume so a lane is released while a person answers, then resumed before new work
- A child-process environment allowlist and fail-closed checks on who may edit a Jira issue

## Not in the published engine

The engine working tree on this machine has uncommitted edits that let a platform use its own git checkout. Those edits are not in `0e1693d` and are not described as a Fleet capability on the other pages.

A comment inside the review loop still says the automatic fix-round default is 2. The configured default is 3, and high-priority or shell tasks use at most one. The pages state the constant.

The engine's own policy text says spec, plan, and merge review are never automatic. The lane path accepts the plan, opens a pull request by default, and can approve a spec on timeout. Those pages follow the code. Merge stays manual unless `auto_merge` is enabled.
