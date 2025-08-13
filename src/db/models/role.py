from src.db.base import Base
from sqlalchemy import Column, String, Integer, func, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    permissions = Column(String(255), nullable=True)
    created_date = Column(DateTime, server_default=func.now(), nullable=False)
    updated_date = Column(DateTime, server_default=func.now(), onupdate=datetime.now(), nullable=False)

    users = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role(name={self.name}, description={self.description})>"
