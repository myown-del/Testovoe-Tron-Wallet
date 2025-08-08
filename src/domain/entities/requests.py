from dataclasses import dataclass
from datetime import datetime
from src.domain.entities.common import Entity


@dataclass
class WalletRequest(Entity):
    wallet_address: str
    created_at: datetime | None = None
