"""Pytest configuration helpers.

Ensure the project's `src` directory is on sys.path during test collection so
tests can import the `calculator` package directly (without setting PYTHONPATH).
"""
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    # Insert at position 0 so local package shadows any installed package.
    sys.path.insert(0, str(SRC))
