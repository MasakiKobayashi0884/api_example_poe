from enum import Enum

from fastapi import APIRouter
from pydantic import BaseModel


class Dir(str, Enum):
    ALPHA = 1
    BRAVO = 2
    CHARY = 3
    OTHER = 999


class EnumModel(BaseModel):
    var: Dir


router = APIRouter(prefix="/enum")


@router.post("/enum_io")
def enum_io(body: EnumModel) -> EnumModel:
    return body
