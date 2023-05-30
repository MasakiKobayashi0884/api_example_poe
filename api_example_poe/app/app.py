from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from api_example_poe.app.api.v1.router import router
from api_example_poe.core.logger import write_request_log

app = FastAPI(
    description="""\
Global description

FastAPIを使ったAPIサーバー、及びその周辺機能についての検証などを行っています。

**参考リンク**

* [FastAPI](https://fastapi.tiangolo.com/ja/)
""",
)

app.include_router(router)
app.add_middleware(BaseHTTPMiddleware, dispatch=write_request_log)
