# Illustrative walkthrough

**Illustrative walkthrough.** The engine repository has no shareable production log. Runtime artifacts and tracker state are local, and real issue text would be customer data. What follows is two acceptance scenarios, told with generic names. They drive the planner, communications loop, queue, architect hook, and tracker against a fake Jira. Model calls and git hosting are stubbed.

No duration, pass rate, or production volume is stated. None was measured for publication.

## 1. Module brief, with a direct issue beside it

### Input

A module brief, `invoice-status`, sits in the docs hub. Its front matter names one tracker issue, so questions and the spec decision are mirrored there. A second brief is waiting. Three direct issues are ready. One of them has an open question in the task text.

### Analysis

The architect reads `invoice-status`, parks the question, and in the same tick analyses the second brief as far as the spec decision. The open-question issue is claimed, then parked before planning. The other two ready issues fill the two lanes in that same tick.

A person answers on the tracker. The communications loop does not apply the comment until the poll interval has elapsed. A later poll does not apply it again. The architect resumes `invoice-status` with that answer before starting a newly arrived brief. The parked issue resumes on the first free lane before a newly arrived issue.

The spec-ready comment says how to approve, revise, or reject, and it states the timeout rule. The scenario approves. Slack, the docs hub, and a Jira comment each produce the same resolved state. The first valid answer wins. The module is finalized only after that approval.

The scenario does not store a real spec body. Separately, the scheduler will not start a task whose `depends_on_tasks` are unfinished. That rule is in the queue tests, not in a captured spec from this run.

### Development, test, and review

Once approved, the module task is assigned to a free lane. The direct issue, after its answer, reaches the plan step in this scenario. It is not taken through merge here. The mirrored tracker issue stays in its original status. Fleet does not transition a module mirror. Progress is a status comment on that issue, and the comment names the module task.

### Result the test checks

Comments on the mirrored issue are one question, its resolution, one spec request, its resolution, and one status comment, in that order. The module continuation is done. The second brief is still waiting on its spec decision. The direct issue is back in progress after the question, and it has a plan comment.

## 2. Direct issue through merge

### Input

A ready task has acceptance criteria and maps to a web lane. Two lanes are free. The pull-request approval gate is switched on for this scenario so a person is asked in the middle. With the default switches that question is not asked, and the pull request opens after a clean review.

### Path

The task is claimed and planned, implemented, and reviewed. At the pull-request gate the worker suspends and the lane goes idle. The next ready issue starts on that lane. A person comments an approval. The original task resumes on a free lane before any newer issue. The pull request opens. The fake CI check is marked green, then the pull request is marked merged.

### Result the test checks

The status sequence is In Progress, Blocked while the gate is open, In Progress again, In Review when the pull request exists, and Done after merge with green CI. Each lifecycle comment is posted once. The living status comment is edited in place. The continuation is consumed. A restart before any step still ends in that state. Replaying a step does not duplicate the comments.

## What this is evidence of

These scenarios are evidence about control flow under stubs: parking, channel priority, resume order, comment idempotence, and the Done rule. They are not evidence about a live product, a model, or a team.

A third scenario runs two stories and one direct issue together. The direct issue reaches Done while one story is still waiting on a question. Sub-tasks are created only for the story that has been approved. After both are approved and their pull requests are merged with green CI, each parent reaches Done once. That scenario is not retold step by step. The [workflow page](workflows.md) describes the path.
