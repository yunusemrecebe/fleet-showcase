# LinkedIn text

Paste-ready English. Counts were measured for this file. No metrics are included.

## Project

**Name** (33 characters)

Fleet — SDLC orchestration engine

**Headline** (113 characters)

Turns a module brief, or a ready Jira task, bug, story, or epic, into reviewed pull requests with explicit gates.

**Description** (1,256 characters, including the blank lines between paragraphs)

Fleet is an SDLC orchestrator I extracted from an upstream engine and generalized. Product code stays in the product repositories. Fleet schedules the path from input to pull request.

Work enters in three ways. A module brief is analysed into a spec and a task list. A ready Jira task or bug, with acceptance criteria and a clear lane, becomes one implementation task. A ready story or epic goes through the same architect path, then its tasks are mirrored as sub-tasks that respect dependencies.

The lane does not block on a person. Questions and spec decisions are parked, other ready work continues, and the parked item resumes first when an answer arrives. QA and Security review the diff and the tests. They are not given the developer transcript. A pull request targets a feature branch. Merging stays with a person unless that automation is turned on. A Jira issue reaches Done only after merge and green CI.

Intake is filtered. Empty reporter allow-lists, human assignees, missing acceptance criteria, unmet blockers, and hold labels are skipped. Jira writes are off until enabled.

The public description covers the behaviour I could verify in the source. It states no success rate and no production volume. The engine is alpha and proprietary.

## Featured

**Title** (23 characters)

Fleet SDLC orchestrator

**Card text** (245 characters)

Fleet is an SDLC orchestrator I extracted and generalized. A module brief or a ready Jira issue goes through spec, implementation, review, and a pull request. People keep the spec decision and the merge. It leaves issues a teammate already owns.

## Skills line

Optional, under the project. Keep it factual:

Python, LangGraph, Jira, GitHub pull requests, SDLC automation, human-in-the-loop systems

## What to leave out

- Upstream organization and product name. Add them only if you want that affiliation public. The engine repo records them.
- Customer issue text, workspace URLs, and tokens.
- Any figure for speed, success rate, or production use. None is published because none was measured for this page.
