from typing import AsyncIterable

from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, AsyncEngine

from src.infrastructure.db.repositories.requests import RequestsLoggingRepository
from src.application.abstractions.repositories import IRequestsLoggingRepository
from src.application.abstractions.config.models import IDatabaseConfig
from src.infrastructure.db.connection import create_engine, create_session_maker


class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self, config: IDatabaseConfig) -> AsyncIterable[AsyncEngine]:
        engine = create_engine(config)
        try:
            yield engine
        finally:
            await engine.dispose()

    @provide
    def get_pool(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self, pool: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with pool() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

    requests_logging_repository = provide(
        RequestsLoggingRepository, scope=Scope.REQUEST, provides=IRequestsLoggingRepository
    )
