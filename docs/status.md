# Current status

Checked against the engine working tree on 23 October 2026, including uncommitted edits. The package version is `0.1.0.dev0`. Its classifiers mark it alpha and private. It is not a published package. No success rate, throughput, or production-usage figure is stated here, because this repository has none to cite.

## Working

These behaviours are implemented in the engine and have tests there.

- Module intake. Briefs are discovered from an allow-list, the docs hub, an approved portfolio file, or a submitted free-input entry. The architect can ask questions, write a spec and tasks, and park one module while analysing another. The parked-spec cap defaults to 3.
- Dependency-aware scheduling. A task waits until the tasks it depends on are done. Non-backend tasks can also wait on named backend tasks.
- Jira task and bug intake. The poll, the filters on this page's sibling [workflows](workflows.md), the claim lease, and the status path through in-progress and in-review are implemented. Done requires a merged pull request and, by default, green CI.
- Jira story and epic intake. The issue becomes a brief, the existing architect handles it, and approved tasks are mirrored as sub-tasks with blocker links. Generated sub-tasks are not ingested again.
- Lane execution. Plan, implement in a worktree, tests, quality gates, then QA, Security, and BA. Pull requests target a feature branch.
- Non-blocking questions. The lane is released, the answer can arrive from Slack, the docs hub, or Jira, and resume runs before new work.
- Crash-safe state. Atomic locked writes, outbox replay, lease expiry, and quarantine of a corrupt interaction store.
- Context isolation for QA and Security, as described in [architecture](architecture.md).
- Child-process environment allowlist, so token-like variables are not inherited by agent, build, test, and git subprocesses.
- Acceptance scenarios that restart between steps and check the direct-issue lifecycle and the module question-and-approval path.

## Partial

Implemented, with a default that limits or changes the behaviour.

- Jira writes default to off. Until writes are enabled, Fleet observes and does not claim or create sub-tasks. A single-host escape hatch exists and the doctor warns about it.
- Spec approval asks a person, then auto-approves on timeout unless that switch is turned off. The overnight window uses a much shorter wait.
- The lane path accepts the implementation plan. Human plan review is the single-task command with auto-approve left off, and the older per-feature graph.
- Pull-request approval defaults to off. The pull request opens after review. Merge automation defaults to off.
- The first automatic fix rounds do not each wait for a person. The configured default is 3, and high-priority or shell tasks use at most one. A comment in the review loop still says the default is 2. The round cap still stops the loop. Finding-triage timeout defaults to approving the fix.
- Exploratory QA after a feature is in the tree and defaults to off.
- Quality gates exist and each can be disabled with an environment switch.
- One product pack still carries product-specific stack settings. The engine profile is generic; that pack is how one product keeps its previous behaviour.
- Per-platform git checkouts are implemented in the working tree, with doctor checks and tests, and are not in the last commit. Without that change, every platform uses the one product repository.
- The per-feature LangGraph path and the lane path disagree on plan and pull-request defaults. Operators running the lane path should use the defaults in [architecture](architecture.md).

## Planned

Listed in the engine roadmap, and not present as a finished capability.

- A hosted runner. Today the engine is a process on a workstation or host, with a documented handoff of state between hosts.
- Further portfolio-intake automation. Drafting a module order exists; the roadmap still calls the human gate around that draft unfinished business.
- Broader product-neutral cleanup of rules and checklists. Packs and stack options are the mechanism already in use.

## Known limitations

- An empty reporter allow-list takes no Jira issue. That is intentional.
- A task or bug with no acceptance criteria, an ambiguous lane, or a human assignee is skipped.
- A story or epic assigned to a person is skipped. Editing it after the spec is generated stops the flow until a person asks for a revise.
- Fleet does not move an issue back after a person moves it, and it does not push the base branch.
- A repository with no CI checks does not reach Jira Done while CI is required.
- Attempt budget defaults to 2. After that the issue is blocked and needs an explicit retry.
- Module questions have no timeout answer. A docs-hub write failure retries. The architect does not fill the gap with assumptions.
- Unrecognised approval replies are ignored on the lane path. Someone must send a recognised approve, reject, or revise.
- Model output can be wrong. Gates and the decisions above are the controls. They are not a measure of how often the model is right.
- This description omits the upstream organization name. The engine repository keeps that attribution with the base commit.

## Engine docs that disagree with the code

Recorded so a reader of the engine does not import the stronger claim.

- Engine policy and the engine architecture page say spec, plan, and merge-review checkpoints are never automated. The lane path auto-accepts plans, auto-opens pull requests, and auto-approves a spec on timeout by default. Merge stays manual unless enabled.
- The engine architecture page centers the LangGraph diagram and does not describe Jira or suspend/resume. The operations notes do. Both are in the source.
- The engine architecture page shows a single product checkout. The working tree also supports a checkout per platform, undocumented by that page and documented by an untracked operator guide in the engine repo.
