from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models import Config


class ConfigDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_config(self) -> Config | None:
        result = await self.db_session.execute(select(Config).limit(1))
        return result.scalar_one_or_none()

    async def create_config(self, cdn_host: str, ratio: int) -> Config:
        config = await self.get_config()
        if config:
            config.cdn_host = cdn_host
            config.ratio = ratio
        else:
            config = Config(cdn_host=cdn_host, ratio=ratio)
            self.db_session.add(config)
        return config
