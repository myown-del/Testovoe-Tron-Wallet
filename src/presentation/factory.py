from fastapi import FastAPI

from src.config.models import APIConfig
from src.presentation import middlewares
from src.presentation.exceptions import register_exception_handlers
from src.presentation.routes import register_routes


def create_bare_app(config: APIConfig) -> FastAPI:
    app = FastAPI()

    app.middleware("http")(middlewares.access_log_middleware)

    register_routes(app=app, config=config)
    register_exception_handlers(app=app)

    return app
