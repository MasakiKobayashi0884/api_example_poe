# ruff: noqa: S602, S607

import subprocess
from pathlib import Path

SOURCE = """\
# ruff unsorted imports
import sys
import os

import fastapi

# ruff/mypy non-annotated def
def non_annotated(a, b):
    pass


# mypy type error
a = 1
b = "2"

a += b

# black unformatted code
c = 314 *         159
"""

path = Path("dirty.py")


def generate() -> None:
    path.write_text(SOURCE)


def remove() -> None:
    path.unlink(missing_ok=True)


if __name__ == "__main__":
    generate()

    subprocess.run("bash scripts/format.sh", shell=True)
    input("ok?")

    remove()
