"""
環境変数の読み込みはpydantic.BaseSettingsを利用して行う。
"""

from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_NAME = "api_example_poe"
    ROOT = Path(__file__).parent.parent.parent
    SERVICE_ROOT = ROOT
    DEVELOP: bool = False
    RESOURCE = ROOT / "resource"

    LOG_DIR = Path("/var/log") / API_NAME
    TMP_DIR: Path | None = None

    SERVER_PORT: int = 7000
    SERVER_HOST: str = "127.0.0.1"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
