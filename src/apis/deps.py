from typing import Annotated, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import async_session


async def get_db()->AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get a database session.
    """
    async with async_session() as session:
        yield session