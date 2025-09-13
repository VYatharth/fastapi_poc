
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from my_app.data.core import DbBase
from my_app.data.db_models.db_department import DbDepartment


class DbUser(DbBase):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    email: Mapped[str] = mapped_column(String(500), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    department_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("departments.id", ondelete="SET NULL")
    )

    department: Mapped[DbDepartment | None] = relationship(back_populates="users")

    def __repr__(self):
        return f"<DbUser(id='{self.id}', email='{self.email}', name='{self.name}', department_id='{self.department_id}')>"
