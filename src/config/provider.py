from dishka import Provider, Scope, provide, from_context

from src.application.abstractions.config.models import IDatabaseConfig
from src.config.models import APIConfig, Config, TronGridConfig


class ConfigProvider(Provider):
    scope = Scope.APP
    config = from_context(provides=Config, scope=Scope.APP)

    @provide
    def get_api_config(self, config: Config) -> APIConfig:
        return config.api
    
    @provide
    def get_tron_grid_config(self, config: Config) -> TronGridConfig:
        return config.tron_grid


class DatabaseConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def get_db_config(self, config: Config) -> IDatabaseConfig:
        return config.db
