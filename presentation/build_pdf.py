#!/usr/bin/env python3
"""Render presentation/deck.html to presentation/fleet-showcase.pdf."""

from __future__ import annotations

import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML = HERE / "deck.html"
PDF = HERE / "fleet-showcase.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def main() -> None:
    if not HTML.is_file():
        raise SystemExit(f"missing {HTML}")
    PDF.unlink(missing_ok=True)
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={PDF}",
            HTML.as_uri(),
        ],
        check=True,
    )
    if not PDF.is_file() or PDF.stat().st_size < 1000:
        raise SystemExit("PDF was not written")
    print(f"wrote {PDF} ({PDF.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
