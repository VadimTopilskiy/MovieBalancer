from fastapi import APIRouter
from api.config import config_router
from api.redirect import redirect_router

routers = APIRouter()
routers.include_router(config_router, prefix="/config", tags=["config"])
routers.include_router(redirect_router, tags=["redirect"])