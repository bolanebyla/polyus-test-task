from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .settings import DBSettings


def create_engine_from_settings(settings: DBSettings) -> AsyncEngine:
    return create_async_engine(settings.DB_URL, echo=settings.DB_ECHO)


def create_session_factory(
    engine: AsyncEngine
) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    return session_factory
