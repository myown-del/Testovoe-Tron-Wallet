from typing import AsyncGenerator

import pytest_asyncio
from dishka import AsyncContainer

from fastapi import FastAPI
from httpx import AsyncClient
from dishka.integrations import fastapi as fastapi_integration
from src.config.models import APIConfig
from src.presentation.factory import create_bare_app


@pytest_asyncio.fixture(scope="session")
async def app(dishka: AsyncContainer) -> FastAPI:
    api_config = await dishka.get(APIConfig)
    app_ = create_bare_app(config=api_config)
    fastapi_integration.setup_dishka(container=dishka, app=app_)
    return app_


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

