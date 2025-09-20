from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from my_app.data.core import get_db
from my_app.data.repositories.user_repository_impl import UserRepositoryImpl
from my_app.domain.repository_interfaces.user_repository import IUserRepository
from my_app.domain.service.user_service import UserService
from my_app.data.repositories.department_repository_impl import (
    DepartmentRepositoryImpl,
)
from my_app.domain.repository_interfaces.department_repository import (
    IDepartmentRepository,
)
from my_app.domain.service.department_service import DepartmentService

DbSession = Annotated[Session, Depends(get_db)]


def get_user_repository(session: DbSession) -> IUserRepository:
    return UserRepositoryImpl(session)


def get_user_service(
    user_repo: Annotated[IUserRepository, Depends(get_user_repository)],
) -> UserService:
    return UserService(user_repo)


UserServiceDependency = Annotated[UserService, Depends(get_user_service)]


def get_department_repository(session: DbSession) -> IDepartmentRepository:
    return DepartmentRepositoryImpl(session)


def get_department_service(
    dept_repo: Annotated[IDepartmentRepository, Depends(get_department_repository)],
    user_repo: Annotated[IUserRepository, Depends(get_user_repository)],
) -> DepartmentService:
    return DepartmentService(dept_repo, user_repo)


DepartmentServiceDependency = Annotated[
    DepartmentService, Depends(get_department_service)
]
