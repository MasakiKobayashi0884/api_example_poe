import json
import subprocess
from pathlib import Path

from api_example_poe import app
from api_example_poe.core.config import settings

json_path = Path("docs/openapi.json")
json_path.write_text(json.dumps(app.openapi(), indent=2))
package_name = f"{settings.API_NAME}_api"

crate_path = Path("rust_client") / package_name

args = [
    "docker",
    "run",
    "--rm",
    "-v",
    ".:/local",
    "openapitools/openapi-generator-cli",
    "generate",
    "-i",
    str("/local" / json_path),
    "-g",
    "rust",
    "-o",
    str("/local" / crate_path),
    f"--additional-properties=packageName={package_name}",
    "--additional-properties=bestFitInt=true",
]


subprocess.run(args)  # noqa: S603
