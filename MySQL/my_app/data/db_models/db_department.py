
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from my_app.data.core import DbBase
import my_app.data.db_models.db_user as db_user

class DbDepartment(DbBase):
    __tablename__ = "departments"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(500))

    users: Mapped[list["db_user.DbUser"]] = relationship(back_populates="department")

    def __repr__(self):
        return f"<DbDepartment(id='{self.id}', name='{self.name}')>"
