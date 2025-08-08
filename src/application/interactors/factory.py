from dishka import Provider, Scope, provide

from src.application.interactors.requests_logs import GetRequestsLogsInteractor
from src.application.interactors import (
    GetWalletInfoInteractor,
)


class InteractorProvider(Provider):
    get_wallet_requests_interactor = provide(
        GetWalletInfoInteractor, scope=Scope.REQUEST
    )

    get_requests_logs_interactor = provide(
        GetRequestsLogsInteractor, scope=Scope.REQUEST
    )
