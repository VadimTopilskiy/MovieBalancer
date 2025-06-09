from pydantic import BaseModel

class ConfigSchema(BaseModel):
    cdn_host: str
    ratio: int

    class Config:
        from_attributes = True
