from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from my_app.data.repositories.user_repository_impl import UserRepositoryImpl
from my_app.domain.repository_interfaces.user_repository import IUserRepository
from my_app.domain.service.user_service import UserService
from my_app.data.core import get_db

DbSession = Annotated[Session, Depends(get_db)]


def get_user_repository(session: DbSession) -> IUserRepository:
    return UserRepositoryImpl(session)


def get_user_service(
    user_repo: Annotated[IUserRepository, Depends(get_user_repository)],
) -> UserService:
    return UserService(user_repo)


UserServiceDependency = Annotated[UserService, Depends(get_user_service)]
