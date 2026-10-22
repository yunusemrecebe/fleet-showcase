# Fleet

Fleet is an SDLC orchestrator. A module analysis, or a ready Jira task, bug, story, or epic, goes in. A spec, implementation tasks, tests, review, and a pull request come out. Product code stays in the product repositories. Fleet is the engine beside them: workspace configuration, role rules, and runtime state live next to `fleet.config.yaml`, outside the engine package.

This repository is a public description for recruiters and engineers. The engine source stays in its own codebase. See [NOTICE](NOTICE.md).

## Problem

A feature arrives as a long analysis or as a tracker issue. Someone still has to split it into tasks, honour dependencies, keep review separate from implementation, and tell ready work from everything else in the backlog. Handing every open issue to an agent takes the wrong bugs, including ones a teammate already owns and ones with no acceptance criteria.

## Approach

Fleet schedules that path and records the gates. The model still has to pass tests, review, and the human decisions below. The default source is module analysis. Jira is a second input, used alone or beside modules. Both feed the same lanes.

**Module analysis.** A person supplies a brief. The architect asks when the brief is unclear, writes a spec (what to build) and a task list, and waits for a spec decision. Other modules can be analysed while one is waiting, up to a small cap.

**Jira task or bug.** A poll takes issues in configured ready statuses. A task or bug that passes the selection rules becomes one implementation task. Acceptance criteria are required. There is no architect pass.

**Jira story or epic.** The same poll can take a story or epic. It is briefed and sent through the same architect path. After the spec is approved, Fleet creates sub-tasks and links them so a task waits for the tasks it depends on. The parent is done only when every sub-task is done under the same rules.

On the lane path, a plan is produced and then accepted without a separate human plan review. Implementation runs in a worktree. Tests and quality gates run before review. QA, then Security, then a business-analyst triage, look at the diff, the tests, and the spec. A pull request opens after a clean review unless that automation is turned off. Merging stays with a person unless Jira merge automation is explicitly enabled. A Jira issue reaches Done only after the pull request is merged and CI is green.

When a person is needed, the lane does not sit idle. Fleet records the question, frees the lane, and resumes that work on the next free compatible lane before starting something new. The first valid answer from Slack, the docs hub, or a Jira comment wins.

Jira intake is filtered. An empty reporter allow-list takes nothing. The wrong status, a missing required label, a hold, an issue assigned to a person, unmet blockers, a task or bug with no acceptance criteria, or an unmapped lane are skipped. With writes off, the default, Fleet only reports what it would claim.

## Contribution

The engine history on `main` is eight commits, all authored by Yunus Emre Cebe on 22 October 2026. The first code commit is a mechanical copy and rename of an upstream orchestrator, with the suite not yet fully green. The later commits are the work visible in this history: workspace separated from the package, product-specific code moved into a pack, crash-safe state, Jira intake, non-blocking human interactions, acceptance scenarios, and a security pass on child-process environments and fail-closed tracker checks. An uncommitted local change lets each platform use its own git checkout.

Work done inside the upstream project before that copy is not in this history, so it is left unclaimed.

## Status

The engine is version `0.1.0.dev0`, classified as alpha, and is not published as a package. Module intake, filtered Jira intake, the lane scheduler, review, and suspend/resume are implemented, with acceptance tests in the engine repository. This description states no success rate and no production volume. Details are in [Current status](docs/status.md).

## Read next

| If you have | Read |
|---|---|
| About a minute | The three rows above, then the [diagrams](assets/README.md) |
| Five to ten minutes | [Workflows](docs/workflows.md), then [Architecture](docs/architecture.md) |
| A concrete sequence | [Illustrative walkthrough](docs/case-study.md) |
| A conversation | [Seven slides](presentation/slides.md) ([PDF](presentation/fleet-showcase.pdf)) |
| A LinkedIn field | [Titles and descriptions](linkedin-project.md) |
