# ruff: noqa: S602, S607

import subprocess

from generate_dirty import generate, remove

if __name__ == "__main__":
    generate()

    subprocess.run("bash scripts/format.sh", shell=True)
    input("ok?")

    remove()
