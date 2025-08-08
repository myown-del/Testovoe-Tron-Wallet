from fastapi import Request
from src.domain.entities.requests import WalletRequest
from src.infrastructure.db.models.requests import WalletRequestDB


def get_request_db(request: WalletRequest) -> WalletRequestDB:
    return WalletRequestDB(
        wallet_address=request.wallet_address,
        created_at=request.created_at,
    )


def get_request(request_db: WalletRequestDB) -> WalletRequest:
    return WalletRequest(
        wallet_address=request_db.wallet_address,
        created_at=request_db.created_at,
    )
