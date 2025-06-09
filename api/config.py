from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from service.config import _get_config, _create_config
from db.database import get_db
from schemas.schemas import ConfigSchema

config_router = APIRouter()


@config_router.get("/", response_model=ConfigSchema)
async def read_config(db: AsyncSession = Depends(get_db)):
    config = await _get_config(db)
    if not config:
        raise HTTPException(status_code=404, detail="Config not found")
    return config


@config_router.post("/", response_model=ConfigSchema)
async def create_config(payload: ConfigSchema, db: AsyncSession = Depends(get_db)):
    return await _create_config(db, payload.cdn_host, payload.ratio)


