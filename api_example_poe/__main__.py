import uvicorn

from api_example_poe.app.app import app
from api_example_poe.core.config import settings
from api_example_poe.core.logger import get_logger, setup_logger


def main() -> None:
    setup_logger()

    default_logger = get_logger()
    default_logger.info("Server starting...")
    default_logger.debug(settings)

    uvicorn.run(
        app,
        port=settings.SERVER_PORT,
        host=settings.SERVER_HOST,
    )
    default_logger.info("Server stopped...")


if __name__ == "__main__":
    main()
