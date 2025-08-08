from dishka import FromDishka
from fastapi import APIRouter, Query
from dishka.integrations.fastapi import DishkaRoute

from src.presentation.routes.schemas import TronWalletInfoRead
from src.application.interactors.wallet_info import GetWalletInfoInteractor

router = APIRouter(prefix='/wallets', tags=['Wallets'], route_class=DishkaRoute)


@router.post(
    '/details',
    description='Get wallet info for given address',
    summary='Get wallet info',
    response_model=TronWalletInfoRead,
)
async def get_wallet_info(
    interactor: FromDishka[GetWalletInfoInteractor],
    wallet_address: str = Query(..., description='Wallet address'),
):
    entity = await interactor.execute(wallet_address)
    return TronWalletInfoRead(
        wallet_address=entity.wallet_address,
        balance=entity.balance,
        bandwidth=entity.bandwidth,
        energy=entity.energy,
    )
