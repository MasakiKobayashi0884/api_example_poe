from fastapi import APIRouter

from .endpoints import customize, enum_, health_check, labs, media, params, primitive

router = APIRouter()

sub_routers = [
    health_check.router,
    customize.router,
    enum_.router,
    labs.router,
    media.router,
    params.router,
    primitive.router,
]

for sub_router in sub_routers:
    router.include_router(sub_router)
