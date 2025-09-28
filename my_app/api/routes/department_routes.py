import uuid

from fastapi import APIRouter, HTTPException

from my_app.api.dependencies import DepartmentServiceDependency, UserServiceDependency
from my_app.common.models.department_dtos import CreateDepartmentDto
from my_app.common.models.exceptions import (
    DepartmentNotFoundException,
    DepartmentUpdateException,
)
from my_app.domain.entities.department import Department
from my_app.domain.entities.user import User

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get("/{dept_id}", response_model=Department)
def get_department(
    department_id: str,
    department_service: DepartmentServiceDependency,
):
    department = department_service.get_department(department_id)
    if not department:
        raise DepartmentNotFoundException(department_id)
    return department


@router.get("/", response_model=list[Department])
def get_all_departments(
    department_service: DepartmentServiceDependency,
):
    departments = department_service.get_departments()

    return departments


@router.post("/", response_model=Department)
def create_department(
    department_dto_obj: CreateDepartmentDto,
    department_service: DepartmentServiceDependency,
):
    department_dto_obj.id = str(uuid.uuid4())
    department = Department.model_validate(
        department_dto_obj, from_attributes=True, strict=False
    )
    department = department_service.create_department(department)
    return department


@router.put("/{department_id}", response_model=Department)
def update_department(
    department_update_dto: CreateDepartmentDto,
    department_service: DepartmentServiceDependency,
):
    try:
        department = Department.model_validate(
            department_update_dto, from_attributes=True
        )
        department = department_service.update_department(department)

    except Exception:
        raise DepartmentUpdateException(department_update_dto)
    return department


@router.delete("/{department_id}")
def delete_department(
    department_id: str,
    department_service: DepartmentServiceDependency,
) -> None:
    try:
        department_service.delete_department(department_id)

    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.delete("/get_users/{department_id}")
def get_users_in_department(
    department_id: str,
    department_service: DepartmentServiceDependency,
) -> list[User] | None:
    return department_service.get_users_in_department(department_id)
