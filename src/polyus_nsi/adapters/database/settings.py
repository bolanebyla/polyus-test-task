from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    DB_URL: str
    DB_ECHO: bool = False


class AlembicSettings(BaseSettings):
    # Python путь к каталогу, где лежит запускатор alembic
    # (пример: <project_name>.composites:alembic)
    ALEMBIC_SCRIPT_LOCATION: str = 'polyus_nsi.adapters.database:alembic'

    # Python путь к каталогу с миграциями
    ALEMBIC_VERSION_LOCATIONS: str = 'polyus_nsi.adapters.database:migrations'

    ALEMBIC_MIGRATION_FILENAME_TEMPLATE: str = (
        '%%(year)d_'
        '%%(month).2d_'
        '%%(day).2d_'
        '%%(hour).2d_'
        '%%(minute).2d_'
        '%%(second).2d_'
        '%%(slug)s'
    )
