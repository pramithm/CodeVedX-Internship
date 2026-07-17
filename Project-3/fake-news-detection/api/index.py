"""
Vercel WSGI entry point.

Vercel's Python runtime requires the Flask `app` object to be accessible
from a file inside the `api/` directory.  This module adds the project
root to sys.path so that `from app import app` resolves correctly
regardless of the working directory Vercel uses at runtime.
"""

import sys
import os

# Ensure the project root (parent of this api/ directory) is on sys.path
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from app import app  # noqa: E402  (import after sys.path manipulation)
