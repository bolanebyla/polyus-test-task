from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from polyus_nsi.adapters import database, log
from polyus_nsi.adapters.database.repositories import IndustrialStructureRepo
from polyus_nsi.application.nsi.services import IndustrialStructureService


class DB:
    settings = database.DBSettings()

    engine = database.create_engine_from_settings(settings=settings)
    session_factory = database.create_session_factory(engine=engine)


class Logger:
    log.configure(DB.settings.LOGGING_CONFIG)


async def get_db_session() -> AsyncSession:
    async with DB.session_factory() as session:
        yield session
        await session.commit()


def create_industrial_structure_repo(
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> IndustrialStructureRepo:
    return IndustrialStructureRepo(session=session)


def create_industrial_structure_service(
    industrial_structure_repo: Annotated[
        IndustrialStructureRepo,
        Depends(create_industrial_structure_repo)],
) -> IndustrialStructureService:
    return IndustrialStructureService(
        industrial_structure_repo=industrial_structure_repo
    )
