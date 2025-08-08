from src.application.abstractions.clients import ITronClient
from src.application.abstractions.repositories import IRequestsLoggingRepository
from src.domain.entities.requests import WalletRequest
from src.domain.entities.wallets import TronWalletInfo


class GetWalletInfoInteractor:
    def __init__(self, tron_client: ITronClient, requests_logging_repository: IRequestsLoggingRepository) -> None:
        self.tron_client = tron_client
        self.requests_logging_repository = requests_logging_repository

    async def execute(self, wallet_address: str) -> TronWalletInfo:
        wallet_info = await self.tron_client.get_wallet_info(wallet_address)
        await self.requests_logging_repository.create_wallet_request(
            request=WalletRequest(
                wallet_address=wallet_address,
            )
        )
        return wallet_info
    
