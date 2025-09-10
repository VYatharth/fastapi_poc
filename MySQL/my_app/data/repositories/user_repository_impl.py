from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from my_app.data.db_models.db_user import DbUser
from my_app.data.repositories.base_repository_impl import BaseRepositoryImpl
from my_app.domain.entities.user import User
from my_app.domain.repository_interfaces.user_repository import IUserRepository


class UserRepositoryImpl(BaseRepositoryImpl[DbUser], IUserRepository[DbUser]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, DbUser)

    def add(self, entity: User) -> User:
        db_user = DbUser(**entity.model_dump(exclude_unset=True))
        added_user = self._add(db_user)

        return User.model_validate(added_user, from_attributes=True)

    def update(self, obj: User) -> User:
        data = obj.model_dump(exclude_unset=True)
        self._update(data)
        updated_user = self._get_by_id(obj.id)
        return User.model_validate(updated_user, from_attributes=True)

    # def remove(self, entity_id: str) -> None:
    #     self.remove(entity_id)

    def get_by_id(self, entity_id: str) -> User | None:
        db_user = self._get_by_id(entity_id)
        return User.model_validate(db_user, from_attributes=True) if db_user else None

    def get_by_email(self, email: str) -> User | None:
        db_user = self._session.scalars(
            select(DbUser).where(DbUser.email == email)
        ).first()
        return User.model_validate(db_user, from_attributes=True) if db_user else None

    def list_all(self) -> list[User]:
        # db_users = list(self._session.scalars(select(UserDBModel)).all())
        db_users = self._list_all()
        return [
            User.model_validate(db_user, from_attributes=True) for db_user in db_users
        ]
