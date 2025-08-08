from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedMixin


class WalletRequestDB(Base, CreatedMixin):
    __tablename__ = "wallet_requests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    wallet_address: Mapped[str] = mapped_column(String, nullable=False)
