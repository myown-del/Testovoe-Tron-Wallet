import pytest

from src.application.abstractions.repositories import IRequestsLoggingRepository
from src.domain.entities.requests import WalletRequest


@pytest.mark.asyncio
async def test_create_wallet_request(requests_logging_repository: IRequestsLoggingRepository):
    created = await requests_logging_repository.create_wallet_request(WalletRequest(wallet_address="T123"))
    assert created.wallet_address == "T123"
    assert created.created_at is not None

    items = await requests_logging_repository.get_wallet_requests(limit=1, offset=0)
    assert len(items) == 1
    assert items[0].wallet_address == "T123"
    assert items[0].created_at is not None
