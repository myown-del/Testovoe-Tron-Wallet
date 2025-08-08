from dishka import Provider, Scope, provide

from src.config.models import TronGridConfig
from src.application.abstractions.clients import ITronClient
from src.infrastructure.clients.tron import TronClient


class ClientProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_tron_client(self, tron_grid_config: TronGridConfig) -> ITronClient:
        return TronClient(tron_grid_config.api_key)
