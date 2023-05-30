from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

router = APIRouter(prefix="/pure")


@router.get("/text", response_class=PlainTextResponse)
def text() -> PlainTextResponse:
    return PlainTextResponse("Plaintext Response...")


class StrModel(BaseModel):
    __root__: str


@router.get("/str")
def str_() -> StrModel:
    return StrModel(__root__="string?")


class BytesModel(BaseModel):
    __root__: bytes


@router.get("/bytes")
def bytes_() -> BytesModel:
    return BytesModel(__root__=b"bytes?")
