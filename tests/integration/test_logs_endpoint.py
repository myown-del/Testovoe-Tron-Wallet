import pytest
from httpx import AsyncClient

from src.application.abstractions.repositories import IRequestsLoggingRepository
from src.domain.entities.requests import WalletRequest


@pytest.mark.asyncio
async def test_get_wallet_requests_returns_recent_with_pagination(
    client: AsyncClient,
    requests_logging_repository: IRequestsLoggingRepository
):
    addresses = [f"ADDRESS{i}" for i in range(5)]
    for addr in addresses:
        await requests_logging_repository.create_wallet_request(WalletRequest(wallet_address=addr))

    # First page
    resp1 = await client.get("/api/logs/wallet-requests", params={"limit": 2, "offset": 0})
    assert resp1.status_code == 200
    data1 = resp1.json()
    assert len(data1) == 2
    # Most recent first
    assert data1[0]["wallet_address"] == addresses[-1]
    assert data1[1]["wallet_address"] == addresses[-2]

    # Second page
    resp2 = await client.get("/api/logs/wallet-requests", params={"limit": 2, "offset": 2})
    assert resp2.status_code == 200
    data2 = resp2.json()
    assert len(data2) == 2
    assert data2[0]["wallet_address"] == addresses[-3]
    assert data2[1]["wallet_address"] == addresses[-4]

    # Third page
    resp3 = await client.get("/api/logs/wallet-requests", params={"limit": 2, "offset": 4})
    assert resp3.status_code == 200
    data3 = resp3.json()
    assert len(data3) == 1
    assert data3[0]["wallet_address"] == addresses[0] 