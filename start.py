"""Entrypoint for the libretranslate-py ato capsule.

Adds the uv-managed venv's site-packages to sys.path so we don't depend on
ato's `uv run` wrapper preserving the venv at exec time.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VENV_SITE_PACKAGES = HERE / ".venv" / "lib" / "python3.11" / "site-packages"
if VENV_SITE_PACKAGES.exists() and str(VENV_SITE_PACKAGES) not in sys.path:
    sys.path.insert(0, str(VENV_SITE_PACKAGES))


def main() -> None:
    sys.argv = [
        "libretranslate",
        "--host",
        "127.0.0.1",
        "--port",
        "5001",
        "--load-only",
        "ja,en",
        "--update-models",
    ]
    from libretranslate.main import main as libretranslate_main

    libretranslate_main()


if __name__ == "__main__":
    main()
