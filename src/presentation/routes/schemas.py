from datetime import datetime

from pydantic import BaseModel


class TronWalletInfoRead(BaseModel):
    wallet_address: str
    balance: float
    bandwidth: int
    energy: int


class WalletRequestLogRead(BaseModel):
    wallet_address: str
    requested_at: datetime

