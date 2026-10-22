#!/usr/bin/env python3
"""Build presentation/fleet-showcase.pdf from presentation/slides.md.

Standard PDF fonts only (Helvetica). Slide breaks are a line containing ---.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "slides.md"
PDF = HERE / "fleet-showcase.pdf"

PAGE_W = 960
PAGE_H = 540
MARGIN_X = 56
MARGIN_TOP = 64


def parse_slides(text: str) -> list[tuple[str, list[str]]]:
    slides = []
    for chunk in text.split("\n---\n"):
        lines = [ln.rstrip() for ln in chunk.strip().splitlines() if ln.strip()]
        if not lines or not lines[0].startswith("# "):
            raise SystemExit(f"slide is missing a title: {chunk[:80]!r}")
        title = lines[0][2:].strip()
        body = [ln[2:].strip() if ln.startswith("- ") else ln for ln in lines[1:]]
        kinds = [("bullet" if raw.startswith("- ") else "para") for raw in lines[1:]]
        slides.append((title, list(zip(kinds, body))))
    return slides


def wrap(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build(slides: list[tuple[str, list[tuple[str, str]]]]) -> bytes:
    objects: list[bytes] = []

    def add(data: bytes) -> int:
        objects.append(data)
        return len(objects)

    font_regular = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    font_bold = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    page_ids = []
    content_ids = []
    for index, (title, blocks) in enumerate(slides, start=1):
        commands = [
            "0.97 0.96 0.95 rg",
            f"0 0 {PAGE_W} {PAGE_H} re f",
            "0.76 0.25 0.05 rg",
            f"0 {PAGE_H - 8} {PAGE_W} 8 re f",
        ]
        y = PAGE_H - MARGIN_TOP

        def draw(font_id: int, size: int, x: float, yy: float, line: str, gray: float = 0.11) -> None:
            commands.append(f"BT /F{font_id} {size} Tf {gray:.2f} {gray:.2f} {gray:.2f} rg")
            commands.append(f"1 0 0 1 {x:.1f} {yy:.1f} Tm ({pdf_escape(line)}) Tj ET")

        draw(2, 26, MARGIN_X, y, title, gray=0.08)
        y -= 18
        commands.append("0.76 0.25 0.05 rg")
        commands.append(f"{MARGIN_X} {y:.1f} 72 3 re f")
        y -= 28
        for kind, paragraph in blocks:
            width = 78 if kind == "para" else 74
            size = 16 if kind == "para" else 15
            lines = wrap(paragraph, width)
            if kind == "bullet":
                for i, line in enumerate(lines):
                    prefix = "- " if i == 0 else "  "
                    draw(1, size, MARGIN_X, y, prefix + line, gray=0.16)
                    y -= 22
                y -= 6
            else:
                for line in lines:
                    draw(1, size, MARGIN_X, y, line, gray=0.16)
                    y -= 22
                y -= 10
            if y < 48:
                raise SystemExit(f"slide {index} overflows: {title}")
        draw(1, 11, PAGE_W - MARGIN_X - 70, 28, f"{index}  /  {len(slides)}", gray=0.40)
        draw(1, 11, MARGIN_X, 28, "Fleet  ·  public description", gray=0.40)
        stream = "\n".join(commands).encode("latin-1")
        content_ids.append(add(b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream"))
        page_ids.append(None)

    page_obj_ids = []
    for content_id in content_ids:
        page_obj_ids.append(add(
            f"<< /Type /Page /Parent 0 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Contents {content_id} 0 R /Resources << /Font << /F1 {font_regular} 0 R /F2 {font_bold} 0 R >> >> >>".encode()
        ))

    kids = " ".join(f"{pid} 0 R" for pid in page_obj_ids)
    pages_id = add(f"<< /Type /Pages /Count {len(page_obj_ids)} /Kids [{kids}] >>".encode())
    # Parent references were placeholders. Patch page objects now that pages_id is known.
    for pid in page_obj_ids:
        objects[pid - 1] = objects[pid - 1].replace(b"/Parent 0 0 R", f"/Parent {pages_id} 0 R".encode())
    catalog_id = add(f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode())

    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out.extend(f"{i} 0 obj\n".encode())
        out.extend(obj)
        out.extend(b"\nendobj\n")
    xref = len(out)
    out.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    out.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode())
    out.extend(
        f"trailer << /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    )
    return bytes(out)


def main() -> None:
    slides = parse_slides(SLIDES.read_text(encoding="utf-8"))
    if not 6 <= len(slides) <= 8:
        raise SystemExit(f"expected 6-8 slides, got {len(slides)}")
    PDF.write_bytes(build(slides))
    print(f"wrote {PDF} ({len(slides)} pages)")


if __name__ == "__main__":
    main()
