from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=False)
    dob = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)

    created_date = Column(DateTime, server_default=func.now(), nullable=False)
    updated_date = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    password_hash = Column(String(128), nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    role = relationship("Role", back_populates="users")




