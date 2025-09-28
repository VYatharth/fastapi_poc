import uuid

from fastapi import APIRouter, HTTPException

from my_app.domain.entities.department import Department
from my_app.api.dependencies import UserServiceDependency, DepartmentServiceDependency
from my_app.common.models.exceptions import UserUpdateException, UserNotFoundException
from my_app.common.models.user_dtos import CreateUserDto
from my_app.domain.entities.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}", response_model=User)
def get_user(
    user_id: str,
    user_service: UserServiceDependency,
):
    user = user_service.get_user(user_id)
    if not user:
        raise UserNotFoundException(user_id)
    return user


@router.get("/", response_model=list[User])
def get_all_users(
    user_service: UserServiceDependency,
):
    users = user_service.get_users()

    return users


@router.post("/", response_model=User)
def create_user(
    user_dto_obj: CreateUserDto,
    user_service: UserServiceDependency,
):
    user_dto_obj.id = str(uuid.uuid4())
    user = User.model_validate(user_dto_obj, from_attributes=True, strict=False)
    user = user_service.create_user(user)
    return user


@router.put("/{user_id}", response_model=User)
def update_user(
    user_update_dto: CreateUserDto,
    user_service: UserServiceDependency,
):
    try:
        user = User.model_validate(user_update_dto, from_attributes=True)
        user = user_service.update_user(user)

    except Exception:
        raise UserUpdateException(user_update_dto)
    return user


@router.delete("/{user_id}")
def delete_user(
    user_id: str,
    user_service: UserServiceDependency,
) -> None:
    try:
        user_service.delete_user(user_id)

    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/get_department/{user_id}")
def get_department_for_user(
    user_id: str,
    department_service: DepartmentServiceDependency,
) -> Department | None:
    return department_service.get_department_for_user(user_id)
