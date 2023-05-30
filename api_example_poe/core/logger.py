import logging
import sys
import time
from collections.abc import Awaitable, Callable
from datetime import datetime, timedelta, timezone
from functools import cache
from logging.handlers import TimedRotatingFileHandler

from fastapi import Response
from fastapi.requests import Request

from .config import settings

JST = timezone(timedelta(hours=9))
CallNextType = Callable[[Request], Awaitable[Response]]


def get_logger() -> logging.Logger:
    return logging.getLogger(settings.API_NAME)


def get_health_check_logger() -> logging.Logger:
    return logging.getLogger(settings.API_NAME + "_health_check")


@cache
def setup_logger() -> None:
    default_logger = get_logger()
    health_check_logger = get_health_check_logger()

    if not settings.LOG_DIR.exists():
        default_logger.warning("make directory for logging at %s", settings.LOG_DIR)
        settings.LOG_DIR.mkdir(parents=True, exist_ok=True)

    if settings.DEVELOP:
        default_logger.setLevel(logging.DEBUG)
        health_check_logger.setLevel(logging.DEBUG)
    else:
        default_logger.setLevel(logging.INFO)
        health_check_logger.setLevel(logging.INFO)

    formatter = logging.Formatter("API:%(levelname)-7s[%(asctime)s] %(message)s")
    formatter.converter = lambda _: datetime.now(tz=JST).timetuple()

    # file
    file_handler = TimedRotatingFileHandler(
        settings.LOG_DIR / "request.log",
        when="D",
        interval=1,
        backupCount=31,
    )
    file_handler.setFormatter(formatter)
    default_logger.addHandler(file_handler)

    # stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    default_logger.addHandler(stdout_handler)
    health_check_logger.addHandler(stdout_handler)

    # output for /health_check
    health_check_file_handler = logging.FileHandler(settings.LOG_DIR / "health_check.log")
    health_check_file_handler.setFormatter(formatter)
    health_check_logger.addHandler(health_check_file_handler)


def repr_client(client: list[str | int] | None) -> str:
    if not client:
        return ""
    address, port, *_ = client
    return f"{address}:{port}"


async def write_request_log(request: Request, call_next: CallNextType) -> Response:
    logger = get_logger() if request.scope["path"] != "/health_check" else get_health_check_logger()

    logger.info(
        "Request : %s - %s - %s",
        repr_client(request.scope.get("client")),
        request.scope["method"],
        request.scope["path"],
    )

    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()

    logger.info(
        "Response: %s - %.4fs",
        response.status_code,
        end_time - start_time,
    )

    return response
