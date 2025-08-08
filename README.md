## Эндпоинты

1. `POST /api/wallets/details` - Получить информацию об адресе

    Возвращает в теле поля:
    - `wallet_address: str`
    - `bandwith: int`
    - `energy: int`
    - `balance: float`

<br>

2. `GET /api/logs/wallet-requests` - Получить логи запросов об адресах

    Принимает query params:
    - `offset: int`
    - `limit: int`

    Возвращает в теле список из структур, содержащих:
    - `wallet_address: str`
    - `requested_at: datetime`


## Как запускать микросервис
0. Скопировать `env_example`, переименовав его в `.env` и заполнив параметры.

   > TRON_GRID__API_KEY - API-ключ из сервиса https://www.trongrid.io/
2. Выполнить `make start-db`
3. Выполнить `make migrate`
4. Выполнить `make start`

## Как запустить тесты
Выполнить `make test`
