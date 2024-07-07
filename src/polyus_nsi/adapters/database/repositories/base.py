from attr import frozen
from sqlalchemy.ext.asyncio import AsyncSession


@frozen
class AsyncBaseRepo:
    session: AsyncSession
