from src.db.base import Base
from sqlalchemy import Column, String, Integer



class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
