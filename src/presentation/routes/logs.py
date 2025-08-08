from dishka import FromDishka
from fastapi import APIRouter, Query
from dishka.integrations.fastapi import DishkaRoute

from src.presentation.routes.schemas import WalletRequestLogRead
from src.application.interactors.requests_logs import GetRequestsLogsInteractor

router = APIRouter(prefix='/logs', tags=['Logs'], route_class=DishkaRoute)


@router.get(
    '/wallet-requests',
    description='Get wallet requests',
    summary='Get wallet requests',
    response_model=list[WalletRequestLogRead],
)
async def get_wallet_info(
    interactor: FromDishka[GetRequestsLogsInteractor],
    limit: int = Query(10, description='Limit'),
    offset: int = Query(0, description='Offset'),
):
    entities = await interactor.execute(limit, offset)
    return [WalletRequestLogRead(
        wallet_address=entity.wallet_address,
        requested_at=entity.created_at,
    ) for entity in entities]
