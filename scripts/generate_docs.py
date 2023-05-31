import json
from pathlib import Path

from api_example_poe import app

json_path = Path("docs/openapi.json")
json_path.write_text(json.dumps(app.openapi(), indent=2))
