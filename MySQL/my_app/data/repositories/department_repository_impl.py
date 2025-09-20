from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from my_app.data.db_models.db_department import DbDepartment
from my_app.data.db_models.db_user import DbUser
from my_app.data.repositories.base_repository_impl import BaseRepositoryImpl
from my_app.domain.entities.department import Department
from my_app.domain.repository_interfaces.department_repository import (
    IDepartmentRepository,
)


class DepartmentRepositoryImpl(
    BaseRepositoryImpl[DbDepartment], IDepartmentRepository[DbDepartment]
):
    def __init__(self, session: Session) -> None:
        super().__init__(session, DbDepartment)

    def add(self, entity: Department) -> Department:
        db_dept = DbDepartment(**entity.model_dump(exclude_unset=True))
        added_dept = self._add(db_dept)

        return Department.model_validate(added_dept, from_attributes=True)

    def update(self, obj: Department) -> Department:
        data = obj.model_dump(exclude_unset=True)
        self._update(data)
        updated_dept = self._get_by_id(obj.id)
        return Department.model_validate(updated_dept, from_attributes=True)

    def get_by_id(self, entity_id: str) -> Department | None:
        db_dept = self._get_by_id(entity_id)
        return (
            Department.model_validate(db_dept, from_attributes=True)
            if db_dept
            else None
        )

    def get_department_for_user(self, user_id: str) -> Department | None:
        
        # db_user = self._session.scalars(
        #     select(DbUser).options(lazyload(DbUser.department))
        # ).first()
        
        # to load eagerly
        db_user = self._session.scalars(
            select(DbUser).options(joinedload(DbUser.department, innerjoin=True)).where(DbUser.id == user_id)
        ).first()
        
        # db_dept = self._session.scalars(
        #     select(DbDepartment).options(joinedload(DbDepartment.users.and_(DbUser.id == user_id), innerjoin=True))
        # ).first()

        return (
            Department.model_validate(db_user.department, from_attributes=True)
            if db_user and db_user.department
            else None
        )

    def list_all(self, **filters) -> list[Department]:
        db_depts = self._list_all(**filters)
        return [
            Department.model_validate(db_dept, from_attributes=True)
            for db_dept in db_depts
        ]
