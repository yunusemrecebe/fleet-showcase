# Current status

Checked against published engine revision `0e1693d` (22 October 2026). The package version is `0.1.0.dev0`. Its classifiers mark it alpha and private. It is not a published package.

No success rate, throughput, or production volume is stated. This repository has none to cite.

## In the published engine

- Module intake from an allow-list, the docs hub, an approved portfolio file, or a submitted free-input entry. The architect can ask questions, write a spec and tasks, and park one module while analysing another. The parked-spec cap defaults to 3.
- Dependency-aware scheduling. A task waits until its dependencies are done. Non-backend tasks can also wait on named backend tasks.
- Jira task and bug intake, with the filters in [Workflows](workflows.md), a claim lease, and status moves through in progress and in review. The task skips the architect.
- Jira story and epic intake. The issue becomes a brief for the same architect. Approved tasks are mirrored as sub-tasks with blocker links. Generated sub-tasks are not ingested again.
- Lane execution: plan, implement in a worktree, tests, quality gates, QA, and Security when the task is sensitive. Then BA triage. Pull requests target a feature branch.
- Non-blocking questions. The lane is released. An answer can arrive from Slack, the docs hub, or Jira. Resume runs before new work.
- Crash-safe state: atomic locked writes, outbox replay, lease expiry, and quarantine of a corrupt interaction store.
- Separate review prompts, as described in [Architecture](architecture.md).
- A child-process environment allowlist for agent, build, test, and git subprocesses.
- Acceptance scenarios for the direct-issue lifecycle and the module question-and-approval path. They use a fake tracker and stub the model and git.

## Defaults that change the shape of a run

- Jira writes default to off. Until writes are enabled, Fleet observes and does not claim or create sub-tasks.
- Spec approval asks a person, then auto-approves on timeout unless that switch is turned off. The overnight window uses a 180-second wait.
- The lane path accepts the implementation plan. Human plan review is the single-task command with auto-approve left off, and the per-feature graph.
- Pull-request approval defaults to off, so the pull request opens after review. Merge automation defaults to off.
- Jira Done follows `done_on` and `ci_required`. The defaults require a merged pull request and green CI.
- The first automatic fix rounds do not each wait for a person. The configured default is 3. High-priority or shell tasks use at most one.
- Exploratory QA exists and defaults to off.
- Each quality gate can be disabled with an environment switch.
- One product pack still carries one product's stack settings. The engine profile is generic.
- The per-feature graph and the lane path do not share approval defaults. Use [Architecture](architecture.md) for the lane path.

## Not built

- A hosted runner. The engine is a process on a machine, with a documented handoff of state between hosts.
- A finished automation around drafting a portfolio of modules. Drafting exists. The human gate around that draft is still called out as unfinished in the engine roadmap.
- Measured production use. Nothing in this repository is that measurement.

## Limits

- An empty reporter allow-list takes no Jira issue.
- A task or bug with no acceptance criteria, an ambiguous lane, or a human assignee is skipped. So is a story or epic assigned to a person.
- Editing a story or epic after the spec is generated stops the flow until a person asks for a revise.
- Fleet does not move an issue back after a person moves it, and it does not push the base branch.
- A repository with no CI checks does not reach Jira Done while CI is required.
- The attempt budget defaults to 2. After that the issue is blocked until an explicit retry.
- Module questions have no timeout answer. A failed docs-hub write is retried. The architect does not fill the gap with assumptions.
- Unrecognised approval replies are ignored on the lane path.
- Security review runs only for sensitive tasks, using the rule in [Architecture](architecture.md).
- Model output can be wrong. Gates and the decisions above are the controls. They are not a success rate.
