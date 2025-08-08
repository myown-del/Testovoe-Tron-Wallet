from dataclasses import dataclass

from src.application.abstractions.config.models import IDatabaseConfig


@dataclass
class APIConfig:
    internal_host: str
    port: int
    auto_reload: bool = True
    workers: int = 1


@dataclass
class DatabaseConfig(IDatabaseConfig):
    host: str
    port: int
    database: str
    user: str
    password: str
    engine: str = "postgresql+asyncpg"

    @property
    def uri(self) -> str:
        return f"{self.engine}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class TronGridConfig:
    api_key: str


@dataclass
class Config:
    api: APIConfig
    db: DatabaseConfig
    tron_grid: TronGridConfig
