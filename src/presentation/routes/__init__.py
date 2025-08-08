from fastapi import FastAPI, APIRouter

from src.config.models import APIConfig
from .wallets import router as wallets_router
from .logs import router as logs_router


def register_routes(app: FastAPI, config: APIConfig):
    root_router = APIRouter(prefix='/api')
    root_router.include_router(wallets_router)
    root_router.include_router(logs_router)

    app.include_router(root_router)
