import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from my_app.data.core import DbBase


class UserDBModel(DbBase):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    email: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    department_id: Mapped[str | None] = mapped_column(String(36), nullable=True)

    def __repr__(self):
        return f"<UserDBModel(id='{self.id}', email='{self.email}', name='{self.name}', department_id='{self.department_id}')>"
