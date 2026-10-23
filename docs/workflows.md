# Three intake flows

All three flows end in the same lane: plan, implement, test, review, pull request. They differ in who writes the task list and which issues are eligible. Diagrams: [three intakes](../assets/three-intakes.svg), [Jira selection](../assets/jira-selection.svg), [control points](../assets/control-points.svg).

The default source mode is modules. Jira runs only when the profile says `jira` or `both`. Jira writes default to off, so a first poll observes and claims nothing.

## Side by side

| | Module analysis | Task or bug | Story or epic |
|---|---|---|---|
| Input | A brief in the docs hub, a module file, an approved portfolio list, or a submitted free-input entry | One issue whose type is Task, Bug, or Sub-task | One issue whose type is Story or Epic |
| Who splits the work | The architect, after any clarification questions | Nobody. The issue is already one task | The architect. Approved tasks are mirrored as sub-tasks |
| Acceptance criteria | Come from the brief and the spec | Required, or the issue is skipped | Not required on the issue itself. The spec carries the breakdown |
| Dependencies | `depends_on_tasks` on the generated tasks. The planner waits | "Is blocked by" links. Unfinished blockers skip the issue | Same task dependencies, also written as blocker links on the sub-tasks |
| Human decision before coding | Clarification if the brief is unclear, then a spec decision | None, unless the task text itself contains open questions. The architect is skipped | Same architect gates as a module |
| Tracker updates | Optional mirror onto one tracking issue | Status, comments, and a lease when writes are on | Parent progress, plus one sub-task per generated task |

Issue type names are configuration. The defaults are Task, Bug, and Sub-task for the direct path, and Story and Epic for the spec path.

## What the Jira poll will take

The pickup query is the configured project, the ready statuses, and an optional required label, ordered by priority then creation time. A custom query can replace that. Every candidate then has to pass the filters. Failure skips the issue. With writes on, some skips get one explanatory comment and are not repeated for the same cause.

Shared filters:

- The project key matches.
- The status is a configured ready status. In-progress, in-review, done, and blocked are not picked up as new work.
- The required label is present, when one is configured.
- The hold label is absent, and the issue is not already claimed.
- The reporter, the creator, and every editor of the summary, description, and acceptance criteria are on the allow-list. An empty allow-list allows nobody.
- The change history is complete enough to know who edited the text. A truncated history is a skip.
- Blocker links are Done. An unknown blocker status counts as not done.
- Fleet-generated sub-tasks and module-mirror epics are ignored.

Then the paths split:

- A task or bug must be unassigned, or assigned to the bot account. A person who already owns it is left alone. It must have acceptance criteria, from a description heading or a configured field. Its components or labels must map to exactly one lane. The write scope is the lane root, not paths mentioned in the issue text.
- A story or epic does not need acceptance criteria at pickup. The spec flow still refuses an issue assigned to a person. It writes a brief and registers the architect. At most five new spec issues are ingested per planner tick.

A global pause, or a hold on one issue, stops new claims. Running work stops at the next safe point. Attempts are capped (default 2). Past the cap, the issue is blocked with a comment and is not looped.

Under the default Jira settings, Done requires a merged pull request and green CI. `done_on` and `ci_required` can change that. Opening a pull request moves the issue to in review. A failed or deferred task does not close the issue.

## Module example

A brief for an invoice-status module is placed in the analysis input. The architect reads it. The payment source is unspecified, so it parks a question and moves on to the next brief. A person answers in the docs hub, Slack, or, if the module is mirrored, on the Jira issue. The architect writes a spec with three tasks: the query, the API field, and the filter control. The control depends on the API field. A person approves the spec, or the timeout policy approves it. The planner starts the query and the API field when their dependencies are clear, and holds the control until the API field is done. Each task follows the shared lane path.

An optional portfolio step can draft a module order and wait for a person to approve that order before modules are fed. Discovery also works from an allow-list and from submitted briefs without that draft.

## Task or bug example

A bug, "Status filter returns rows outside the range," sits in Ready for Dev, carries the required label, has an acceptance criterion, and is labeled for the web lane. The reporter is on the allow-list. Nobody is assigned. Blockers are done. The poll claims it, when writes are on, and materializes one task. The lane plans, implements, tests, and reviews. The issue moves to in review when the pull request opens. With the default Jira settings it reaches Done after the pull request is merged and CI is green. `done_on` and `ci_required` can change that rule.

The same bug is skipped if a teammate is the assignee, if the acceptance criterion heading is missing, or if the label maps to two lanes.

## Story or epic example

A story, "Customers filter invoices by status," is in a ready status and passes the shared filters. Fleet writes a brief and runs the architect. Questions and the spec decision are posted to the channels that are enabled, including a comment on the story. After approval, sub-tasks are created under the story, capped (default 40). Dependencies become blocker links. The poller does not ingest those sub-tasks as new work. The parent comment shows progress. The parent reaches Done only when every sub-task has met the Done rule. Under the default Jira settings, that rule is a merged pull request and green CI. `done_on` and `ci_required` can change it.

If someone edits the story after the spec was generated, Fleet stops, comments once, and waits for a revise command. It does not silently rebuild.

## Shared lane, after the task exists

1. Open questions in the task text park the task. The lane takes other work.
2. A plan is generated. On the lane path it is accepted and implementation starts.
3. The worker builds in a worktree and runs tests. Quality gates can fail the task even when the test command exits zero.
4. QA runs from the diff, the test results, and the spec title. Security runs from the diff and the test results only when the task is sensitive. BA triages the findings. Bounded fix rounds may run. The cap ends the loop.
5. A pull request is pushed to a feature branch. The base branch is not the push target. Opening it is separate from merging it.
6. A person merges, unless merge automation was turned on. Under the default Jira settings, Done follows the merge and a green CI result.

The acceptance scenarios that exercise the direct-issue path and the story-or-module path are summarized in the [walkthrough](case-study.md).
