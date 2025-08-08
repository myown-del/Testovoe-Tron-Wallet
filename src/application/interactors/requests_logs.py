from src.application.abstractions.repositories import IRequestsLoggingRepository
from src.domain.entities.requests import WalletRequest


class GetRequestsLogsInteractor:
    def __init__(self, requests_logging_repository: IRequestsLoggingRepository) -> None:
        self.requests_logging_repository = requests_logging_repository

    async def execute(self, limit: int = 10, offset: int = 0) -> list[WalletRequest]:
        return await self.requests_logging_repository.get_wallet_requests(limit, offset)

