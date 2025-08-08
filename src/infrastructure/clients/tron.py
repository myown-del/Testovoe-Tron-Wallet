import asyncio
from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from src.domain.entities.wallets import TronWalletInfo
from src.application.abstractions.clients import ITronClient


class TronClient(ITronClient):
    def __init__(self, api_key: str):
        self.client = AsyncTron(AsyncHTTPProvider(api_key=api_key))
        
    async def get_wallet_info(self, wallet_address: str) -> TronWalletInfo:
        async with self.client as tron:
            bandwidth, energy, balance = await asyncio.gather(
                tron.get_bandwidth(wallet_address),
                tron.get_energy(wallet_address),
                tron.get_account_balance(wallet_address)
            )
            return TronWalletInfo(
                wallet_address=wallet_address,
                bandwidth=bandwidth,
                energy=energy,
                balance=balance,
            )
