from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime


class CreatedMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now, server_default=func.now()
    )
