from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/labs")


class UnionModel(BaseModel):
    data: int | str


@router.post("union")
def union_model(item: UnionModel) -> UnionModel:
    return item
