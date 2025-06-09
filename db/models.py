from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Config(Base):
    __tablename__ = "config"

    id = Column(Integer, primary_key=True)
    cdn_host = Column(String, nullable=False)
    ratio = Column(Integer, nullable=False)
