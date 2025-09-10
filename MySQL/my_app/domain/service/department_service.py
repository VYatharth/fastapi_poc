from my_app.domain.entities.user import User
from my_app.domain.repository_interfaces.user_repository import IUserRepository
from my_app.domain.entities.department import Department
from my_app.domain.repository_interfaces.department_repository import (
    IDepartmentRepository,
)


class DepartmentService:
    def __init__(self, department_repository: IDepartmentRepository, user_repository: IUserRepository):
        self.department_repository = department_repository
        self.user_repository = user_repository

    def get_department(self, dept_id: str):
        return self.department_repository.get_by_id(dept_id)

    def get_departments(self):
        return self.department_repository.list_all()

    def create_department(self, department: Department):
        return self.department_repository.add(department)

    def update_department(self, department: Department):
        return self.department_repository.update(department)

    def delete_department(self, dept_id: str):
        return self.department_repository.remove(dept_id)

    def get_department_for_user(self, user_id: str) -> Department | None:
        return self.department_repository.get_department_for_user(user_id)
    
    def get_users_in_department(self, department_id: str) -> list[User] | None:
        return self.user_repository.list_all(department_id=department_id)
