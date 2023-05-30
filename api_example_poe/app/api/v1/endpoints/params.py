from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/params")


class ParamRespModel(BaseModel):
    path: str
    query: float


@router.get("/{path_p}")
def path_param(path_p: str, query_p: float) -> ParamRespModel:
    return ParamRespModel(path=path_p, query=query_p)
