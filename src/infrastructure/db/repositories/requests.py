from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.abstractions.repositories import IRequestsLoggingRepository
from src.domain.entities.requests import WalletRequest
from src.infrastructure.db.mappers.requests import get_request, get_request_db
from src.infrastructure.db.models.requests import WalletRequestDB


class RequestsLoggingRepository(IRequestsLoggingRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_wallet_requests(self, limit: int = 10, offset: int = 0) -> list[WalletRequest]:
        query = select(WalletRequestDB) \
            .order_by(WalletRequestDB.created_at.desc()) \
            .limit(limit) \
            .offset(offset)
        result = await self.session.execute(query)
        return [
            get_request(request_db)
            for request_db in result.scalars().all()
        ]

    async def create_wallet_request(self, request: WalletRequest) -> WalletRequest:
        request_db = get_request_db(request)
        self.session.add(request_db)
        await self.session.commit()
        await self.session.refresh(request_db)
        return get_request(request_db)

    async def delete_all(self) -> None:
        await self.session.execute(delete(WalletRequestDB))
        await self.session.commit()
