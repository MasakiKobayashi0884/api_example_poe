set -ex

ruff --select I --fix .
black .
