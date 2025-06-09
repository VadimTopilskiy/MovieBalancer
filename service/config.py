from sqlalchemy.ext.asyncio import AsyncSession

from core import env_config
from db.models import Config
from repository.DAL import ConfigDAL


async def _get_config(db: AsyncSession) -> Config:
    config = await ConfigDAL(db).get_config()

    if not config:
        config = await ConfigDAL(db).create_config(
            cdn_host=env_config.CDN_HOST,
            ratio=env_config.DEFAULT_REDIRECT_RATIO
        )
    return config


async def _create_config(db: AsyncSession, cdn_host: str, ratio: int) -> Config:
    async with db.begin():
        dal = ConfigDAL(db)
        return await dal.create_config(cdn_host=cdn_host, ratio=ratio)
