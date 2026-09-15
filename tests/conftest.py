"""Shared setup for the test suite.

Work packages D and E, RQ1. The modules under test live in src/collect,
src/prepare and src/extract. None of these folders is an installed
package, so pytest would not find them. This file adds all three to the
import path before any test module is loaded. pytest reads it
automatically; it is never imported by hand.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

for folder in ("collect", "prepare", "extract"):
    candidate = str(PROJECT_ROOT / "src" / folder)
    if candidate not in sys.path:
        sys.path.insert(0, candidate)
