from typing import Protocol

from src.domain.entities.wallets import TronWalletInfo


class ITronClient(Protocol):
    async def get_wallet_info(self, wallet_address: str) -> TronWalletInfo:
        ...
