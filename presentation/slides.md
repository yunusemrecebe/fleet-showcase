# The handoff is the bottleneck

A feature arrives as a long analysis or as a tracker issue. Someone still has to split the work, honour dependencies, and keep review separate from implementation.

An agent that takes every open issue will take the wrong ones. A teammate may already own it. It may have no acceptance criteria.

---

# Fleet schedules that path

Module analysis is the default input. Jira is a second input. Both feed the same lanes.

Product code stays in the product repositories. Fleet keeps the spec, the task list, the tests, the review, and the pull request.

The model output still has to pass those gates.

---

# Three ways in

- Module brief. The architect asks when the brief is unclear, then waits for a spec decision and a task list.
- Task or bug. Ready status, an allow-listed reporter, acceptance criteria, and one lane. One task. No architect pass.
- Story or epic. The same architect path, then sub-tasks and dependency links. The parent finishes last.

A task starts only when the tasks it depends on are done.

---

# Control points

- A question frees the lane. Answered work resumes before any new work.
- QA and Security see the diff, the tests, and the spec. They do not receive the developer transcript.
- State is written atomically. A crash resumes from saved continuations. Corrupt files are quarantined.
- Spec approval can auto-approve on timeout. The lane path accepts the plan. A person merges unless that switch is on.
- Jira Done waits for a merged pull request and green CI.

---

# A checked sequence

Illustrative. The acceptance tests use a fake tracker. The model and the git host are stubbed.

- A module question parks. The next brief continues in the same tick.
- A direct issue parks on its question. Other ready issues fill the lanes.
- The answer resumes the parked work first. One channel is enough.
- With the pull-request gate on, Done comes after merge and green CI. Restarts do not duplicate comments.

---

# Engineering choices

- Issue text is data. It does not set the write scope.
- An empty reporter allow-list takes nothing. Human assignees are left alone.
- Agent, build, test, and git processes do not inherit token-like environment variables.
- One engine per workspace. Leases expire. Jira writes replay from an outbox, in order.
- Spec rejects, plan rejects, and review rounds hit a cap. The cap is not raised quietly.

---

# Where it stands

- Alpha. The engine is proprietary. This deck is the public description.
- Module intake, filtered Jira intake, lanes, review, and suspend/resume are implemented.
- Jira writes default to off. Pull-request approval defaults to off.
- A checkout per platform exists in the local tree and is not committed yet.
- No success rate and no production volume. Neither was measured for publication.
