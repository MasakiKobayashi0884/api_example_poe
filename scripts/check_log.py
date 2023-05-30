"""
ログ検証用
"""

# ruff: noqa: T201
from fastapi.testclient import TestClient

from api_example_poe import app

client = TestClient(app)
resp = client.get("/health_check")
print("==========RESPONSE==========")
print(resp.status_code)
print(resp.content.decode())
