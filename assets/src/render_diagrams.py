#!/usr/bin/env python3
"""Editable source for the showcase SVGs.

Edit the box labels and coordinates in this file, then run it from the
repository root or from this directory:

    python3 assets/src/render_diagrams.py

It writes the SVGs next to itself and copies them to assets/ for the
README links. The SVGs use only shapes and text, so GitHub can render them.
"""

from __future__ import annotations

import html
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent

INK = "#1c1917"
MUTED = "#57534e"
LINE = "#a8a29e"
PAPER = "#f7f6f3"
CARD = "#ffffff"
HUMAN_FILL = "#fff7ed"
HUMAN_STROKE = "#c2410c"
SKIP_FILL = "#f5f5f4"
SKIP_STROKE = "#78716c"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def text(x: float, y: float, value: str, size: int = 15, fill: str = INK, weight: str = "400", anchor: str = "start") -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="Helvetica, Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{esc(value)}</text>'
    )


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str, rx: float = 10) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
    )


def box(x: float, y: float, w: float, h: float, lines: list[str], fill: str = CARD, stroke: str = LINE, title: bool = False) -> str:
    parts = [rect(x, y, w, h, fill, stroke)]
    size = 15 if title or len(lines) == 1 else 14
    weight = "600" if title or len(lines) == 1 else "400"
    block_h = len(lines) * (size + 4)
    start = y + (h - block_h) / 2 + size - 1
    for i, line in enumerate(lines):
        parts.append(text(x + w / 2, start + i * (size + 4), line, size=size, weight=weight, anchor="middle"))
    return "\n".join(parts)


def header(x: float, y: float, w: float, h: float, label: str, fill: str) -> str:
    return "\n".join([
        rect(x, y, w, h, fill, fill, rx=8),
        text(x + w / 2, y + h / 2 + 5, label, size=15, fill="#ffffff", weight="700", anchor="middle"),
    ])


def varrow(x: float, y1: float, y2: float) -> str:
    return (
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 7}" stroke="{INK}" stroke-width="1.4"/>'
        f'<polygon points="{x - 5},{y2 - 8} {x + 5},{y2 - 8} {x},{y2}" fill="{INK}"/>'
    )


def harrow(x1: float, x2: float, y: float) -> str:
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2 - 7}" y2="{y}" stroke="{INK}" stroke-width="1.4"/>'
        f'<polygon points="{x2 - 8},{y - 5} {x2 - 8},{y + 5} {x2},{y}" fill="{INK}"/>'
    )


def document(width: int, height: int, title: str, body: list[str]) -> str:
    content = "\n".join(body)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
  <title>{esc(title)}</title>
  <rect width="100%" height="100%" fill="{PAPER}"/>
{content}
</svg>
'''


def three_intakes() -> str:
    w, h = 1180, 740
    cols = [32, 406, 780]
    cw = 368
    parts = [
        text(32, 40, "Three ways work enters", size=24, weight="700"),
        text(32, 66, "Orange marks a person. The band at the bottom is shared by all three.", size=15, fill=MUTED),
    ]
    headers = [
        ("Module analysis", "#1e3a5f"),
        ("Task or bug", "#14532d"),
        ("Story or epic", "#7c2d12"),
    ]
    columns = [
        [
            (["Module brief"], False),
            (["Architect"], False),
            (["Questions, if the brief is unclear"], False),
            (["Spec decision"], True),
            (["Task list, with dependencies"], False),
        ],
        [
            (["Ready task or bug"], False),
            (["Selection rules"], False),
            (["Acceptance criteria required"], False),
            (["One implementation task"], False),
            (["The architect is skipped"], False),
        ],
        [
            (["Ready story or epic"], False),
            (["Same architect path"], False),
            (["Questions, if needed"], False),
            (["Spec decision"], True),
            (["Sub-tasks and dependency links"], False),
        ],
    ]
    box_h = 46
    step = 68
    first_y = 128
    for x, (label, color), steps in zip(cols, headers, columns):
        parts.append(header(x, 86, cw, 32, label, color))
        for i, (lines, human) in enumerate(steps):
            y = first_y + i * step
            if i:
                parts.append(varrow(x + cw / 2, y - 16, y - 1))
            parts.append(box(
                x, y, cw, box_h, lines,
                fill=HUMAN_FILL if human else CARD,
                stroke=HUMAN_STROKE if human else LINE,
            ))
        last_bottom = first_y + 4 * step + box_h
        parts.append(varrow(x + cw / 2, last_bottom + 4, 478))

    parts.append(rect(32, 486, 1116, 220, "#ffffff", "#d6d3d1", rx=14))
    parts.append(text(52, 518, "Then one lane", size=18, weight="700"))
    row1 = [
        (52, 230, "Dependencies are done", False),
        (300, 248, "Plan accepted on the lane", False),
        (566, 230, "Implement, test, gates", False),
        (814, 290, "QA, then Security if sensitive", False),
    ]
    for i, (x, pw, label, human) in enumerate(row1):
        parts.append(box(x, 538, pw, 44, [label], fill=HUMAN_FILL if human else CARD, stroke=HUMAN_STROKE if human else LINE))
        if i < 3:
            parts.append(harrow(x + pw + 4, row1[i + 1][0] - 2, 560))
    parts.append(box(52, 612, 360, 48, ["Pull request on a feature branch"]))
    parts.append(harrow(416, 438, 636))
    parts.append(box(440, 612, 220, 48, ["A person merges"], fill=HUMAN_FILL, stroke=HUMAN_STROKE))
    parts.append(harrow(664, 686, 636))
    parts.append(box(688, 612, 420, 48, ["Default Jira Done: merge and green CI"], fill="#f0fdf4", stroke="#166534"))
    return document(w, h, "Three ways work enters Fleet", parts)


def jira_selection() -> str:
    w, h = 1040, 860
    parts = [
        text(40, 42, "Which Jira issues are taken", size=24, weight="700"),
        text(40, 68, "A skip records the cause. It does not change product code.", size=15, fill=MUTED),
    ]
    main_x, main_w = 40, 560
    skip_x, skip_w = 680, 320
    steps = [
        (108, ["Ready status and a supported type", "Required label, not held, not claimed"]),
        (220, ["Reporter, creator, and editors are allowed", "Change history is complete enough to tell"]),
        (332, ["Blockers are Done", "Unknown blocker status still blocks"]),
    ]
    prev_bottom = 88
    for y, lines in steps:
        parts.append(varrow(main_x + main_w / 2, prev_bottom, y))
        parts.append(box(main_x, y, main_w, 78, lines))
        parts.append(harrow(main_x + main_w + 6, skip_x - 2, y + 39))
        prev_bottom = y + 78
    parts.append(rect(skip_x, 108, skip_w, 302, SKIP_FILL, SKIP_STROKE, rx=12))
    parts.append(text(skip_x + 24, 146, "Skip", size=18, weight="700"))
    for i, line in enumerate([
        "Wrong status or type",
        "Missing label, or on hold",
        "Disallowed editor",
        "Open or unknown blocker",
        "One comment if writes are on",
    ]):
        parts.append(text(skip_x + 24, 186 + i * 36, line, size=15, fill=MUTED))

    parts.append(varrow(main_x + main_w / 2, prev_bottom + 4, 460))
    parts.append(box(main_x, 460, main_w, 48, ["Then the issue type splits the path"], title=True))
    parts.append(f'<line x1="320" y1="508" x2="320" y2="528" stroke="{INK}" stroke-width="1.4"/>')
    parts.append(f'<line x1="270" y1="528" x2="770" y2="528" stroke="{INK}" stroke-width="1.4"/>')
    parts.append(box(40, 548, 460, 96, ["Task or bug", "Unassigned, with acceptance criteria,", "mapped to exactly one lane."]))
    parts.append(box(540, 548, 460, 96, ["Story or epic", "Unassigned. Acceptance criteria are", "not required yet. Architect brief."]))
    parts.append(varrow(270, 528, 548))
    parts.append(varrow(770, 528, 548))
    parts.append(box(40, 680, 460, 68, ["One implementation task", "The architect is skipped"]))
    parts.append(box(540, 680, 460, 68, ["Spec decision, then sub-tasks"], fill=HUMAN_FILL, stroke=HUMAN_STROKE))
    parts.append(varrow(270, 644, 680))
    parts.append(varrow(770, 644, 680))
    parts.append(text(40, 778, "Generated sub-tasks and module-mirror issues are never taken as new work.", size=15, fill=MUTED))
    parts.append(text(40, 806, "Writes off: observe only. Empty reporter allow-list: nothing is taken.", size=15, fill=MUTED))
    return document(w, h, "Which Jira issues Fleet takes", parts)


def control_points() -> str:
    w, h = 1180, 760
    parts = [
        text(36, 40, "Control points", size=24, weight="700"),
        text(36, 66, "The lane does not sit and wait. Saved state is what a restart reads.", size=15, fill=MUTED),
    ]
    flow = [
        (96, ["Module brief or ready issue"], False),
        (164, ["Architect for briefs, stories, epics"], False),
        (232, ["Planner assigns a ready task"], False),
        (300, ["Lane: plan, implement, test"], False),
        (368, ["QA, then Security if the task is sensitive"], False),
        (436, ["BA triage"], False),
        (504, ["Pull request on a feature branch"], False),
        (572, ["A person merges"], True),
    ]
    prev = 84
    for y, lines, human in flow:
        parts.append(varrow(230, prev, y))
        parts.append(box(
            36, y, 400, 48, lines,
            fill=HUMAN_FILL if human else CARD,
            stroke=HUMAN_STROKE if human else LINE,
        ))
        prev = y + 48

    notes = [
        (500, 96, "Isolation", [
            "QA gets the diff, test results,",
            "and the spec title. Not the full spec.",
            "Security gets the diff and results",
            "only when the task is sensitive.",
            "Neither gets the developer transcript.",
        ]),
        (840, 96, "While a person answers", [
            "The question is recorded.",
            "The lane is freed.",
            "Other ready work may start.",
            "Parked work resumes first.",
        ]),
        (500, 360, "Recovery", [
            "State files are atomic and locked.",
            "A continuation stores the stage",
            "and the branch.",
            "Corrupt files are quarantined.",
            "Jira writes replay in order.",
        ]),
        (840, 360, "Hard stops", [
            "A person who moves the issue wins.",
            "The base branch is not a push target.",
            "Default Done: merge and green CI.",
            "Hold and pause stop new claims.",
        ]),
    ]
    for x, y, title, lines in notes:
        parts.append(rect(x, y, 304, 230, CARD, "#d6d3d1", rx=12))
        parts.append(text(x + 18, y + 32, title, size=16, weight="700"))
        for i, line in enumerate(lines):
            parts.append(text(x + 18, y + 64 + i * 26, line, size=13, fill=MUTED))
    parts.append(text(36, 700, "Orange is a person. Spec approval can still time out into an approval. The lane path accepts the plan.", size=14, fill=MUTED))
    parts.append(text(36, 726, "Pull-request approval is off unless switched on. Merge stays with a person unless that switch is on.", size=14, fill=MUTED))
    return document(w, h, "Fleet control points", parts)


def main() -> None:
    files = {
        "three-intakes.svg": three_intakes(),
        "jira-selection.svg": jira_selection(),
        "control-points.svg": control_points(),
    }
    for name, svg in files.items():
        (HERE / name).write_text(svg, encoding="utf-8")
        (OUT / name).write_text(svg, encoding="utf-8")
        print(name, len(svg))


if __name__ == "__main__":
    main()
