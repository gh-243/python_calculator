"""Pytest helper to make sure the local `src/` package is importable when
pytest is run with `tests/` as the root directory.
"""
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
