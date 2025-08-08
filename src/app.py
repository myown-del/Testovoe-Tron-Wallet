import logging

from dishka import make_async_container
from dishka.integrations import fastapi as fastapi_integration
from fastapi import FastAPI

from src.infrastructure.clients.provider import ClientProvider
from src.presentation.factory import create_bare_app
from src.config.provider import ConfigProvider, DatabaseConfigProvider
from src.config.models import Config
from src.config.parser import load_config
from src.log import setup_logging
from src.infrastructure.db.provider import DatabaseProvider
from src.application.interactors.factory import InteractorProvider

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    setup_logging()

    config = load_config(
        config_class=Config,
        env_file_path=".env"
    )
    app = create_bare_app(config=config.api)
    container = make_async_container(
        ConfigProvider(),
        DatabaseConfigProvider(),
        DatabaseProvider(),
        InteractorProvider(),
        ClientProvider(),
        context={Config: config}
    )

    fastapi_integration.setup_dishka(container=container, app=app)

    return app