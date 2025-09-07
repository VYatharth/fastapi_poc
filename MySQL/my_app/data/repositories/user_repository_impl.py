from dataclasses import asdict
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from my_app.data.db_models.user import UserDBModel
from my_app.data.repositories.base_repository_impl import GenericRepositoryImpl
from my_app.domain.entities.user import User
from my_app.domain.repository_interfaces.user_repository import IUserRepository


class UserRepositoryImpl(
    GenericRepositoryImpl[UserDBModel], IUserRepository[UserDBModel]
):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def add(self, entity: User) -> User:
        added_user = self._add(asdict(entity))
        return User.model_validate(added_user)

    def update(self, obj: User) -> User:
        data = obj.model_dump(exclude_unset=True)
        updated_user = self._update(data)
        return User.model_validate(updated_user)
    
    def remove(self, entity: User) -> None:
        self._remove(entity.id)

    def get_by_id(self, entity_id: UUID) -> User | None:
        db_user = self._get_by_id(entity_id)
        return User.model_validate(db_user, from_attributes=True) if db_user else None

    def get_by_email(self, email: str) -> User | None:
        db_user = self._session.scalars(
            select(UserDBModel).where(UserDBModel.email == email)
        ).first()
        return User.model_validate(db_user) if db_user else None

    def list_all(self) -> list[User]:
        db_users = self._list_all()
        return [User.model_validate(db_user, from_attributes=True) for db_user in db_users]
