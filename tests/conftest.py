import asyncio
from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from dishka import make_async_container
from alembic.command import upgrade
from dishka import AsyncContainer
from alembic.config import Config as AlembicConfig

from src.infrastructure.clients.provider import ClientProvider
from src.config.provider import ConfigProvider
from src.config.models import Config
from src.config.parser import load_config
from src.infrastructure.db.provider import DatabaseProvider
from tests.fixtures.db_provider import TestDbProvider
from src.application.abstractions.repositories import IRequestsLoggingRepository
from src.application.abstractions.config.models import IDatabaseConfig
from src.application.interactors.factory import InteractorProvider



@pytest_asyncio.fixture(scope="session")
async def dishka():
    config = load_config(
        config_class=Config,
        env_file_path="tests/.env"
    )
    container = make_async_container(
        ConfigProvider(),
        TestDbProvider(),
        DatabaseProvider(),
        InteractorProvider(),
        ClientProvider(),
        context={Config: config}
    )
    yield container
    await container.close()


@pytest_asyncio.fixture(scope="session")
async def alembic_config(dishka: AsyncContainer) -> AlembicConfig:
    alembic_cfg = AlembicConfig("alembic.ini")
    alembic_cfg.set_main_option(
        "script_location",
        str(Path("src") / "infrastructure" / "migrations"),
    )
    db_config = await dishka.get(IDatabaseConfig)
    alembic_cfg.set_main_option("sqlalchemy.url", db_config.uri)
    return alembic_cfg


@pytest.fixture(scope="session", autouse=True)
def upgrade_schema_db(alembic_config: AlembicConfig):
    upgrade(alembic_config, "head")


@pytest_asyncio.fixture
async def dishka_request(dishka: AsyncContainer) -> AsyncGenerator[AsyncContainer, None]:
    async with dishka() as request_container:
        yield request_container


async def clear_db(request_logging_repository: IRequestsLoggingRepository):
    await request_logging_repository.delete_all()


@pytest_asyncio.fixture
async def requests_logging_repository(dishka_request: AsyncContainer) -> AsyncGenerator[IRequestsLoggingRepository, None]:
    repo = await dishka_request.get(IRequestsLoggingRepository)
    yield repo
    await repo.delete_all()
