from typing import Protocol

from src.domain.entities.requests import WalletRequest


class IRequestsLoggingRepository(Protocol):
    async def get_wallet_requests(self, limit: int = 10, offset: int = 0) -> list[WalletRequest]:
        ...

    async def create_wallet_request(self, request: WalletRequest) -> WalletRequest:
        ...

    async def delete_all(self) -> None:
        ...
