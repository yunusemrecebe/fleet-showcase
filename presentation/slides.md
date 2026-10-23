# Fleet — AI SDLC Orchestrator

Yunus Emre Cebe

A multi-agent system that coordinates planning, implementation, testing, review, and pull requests.

https://github.com/yunusemrecebe/fleet-showcase

---

# The handoff is the work

Analysis and tracker issues still need a split, a dependency order, and a review that is separate from the implementer.

Fleet's output is a spec, ordered tasks, tests, a review, and a pull request. A person decides the spec. Under the defaults, a person also merges.

---

# Three ways in

- Module brief. Architect, spec decision, task list.
- Task or bug. Selection rules, one task. The architect is skipped.
- Story or epic. The same architect path, then sub-tasks and dependency links.

A task starts only when the tasks it depends on are done.

---

# Roles and review inputs

- Architect writes the spec. The developer implements one task on a lane.
- QA reads the diff, the test results, and the spec title. Not the full spec, and not the developer transcript.
- Security reads the diff and the test results only when the task is sensitive. It does not receive the QA findings.
- BA triages the findings.

---

# Illustrative flow

Acceptance tests. Fake tracker. The model and git host are stubbed. Not a live delivery.

- A module question parks. The next brief continues in the same tick.
- Answered work resumes before newer work.
- With the pull-request gate on, Done follows a merge and green CI. That is the default Jira rule.
- A restart does not duplicate the comments.

This repository has no saved product diff or pull request to show.

---

# Control that survives a restart

- A question frees the lane. The answered item resumes first.
- State is atomic. Continuations and an outbox survive a crash. Corrupt files are quarantined.
- A person who moves a Jira issue wins. The base branch is not a push target.
- Spec approval can time out into an approval. The lane accepts the plan.
- A pull request opens after review. Merge stays with a person unless that switch is on.

---

# Where it stands

- Alpha engine. This repository is the public description, checked against engine revision 0e1693d.
- Module intake, filtered Jira intake, lanes, and suspend/resume are in that revision.
- Jira writes default to off. Security review is conditional.
- No success rate and no production volume.

Workflows, architecture, and provenance are linked from the README.
