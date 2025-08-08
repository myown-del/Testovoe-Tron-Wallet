from dataclasses import dataclass
from decimal import Decimal
from src.domain.entities.common import Entity


@dataclass
class TronWalletInfo(Entity):
    wallet_address: str
    bandwidth: int
    energy: int
    balance: Decimal
    