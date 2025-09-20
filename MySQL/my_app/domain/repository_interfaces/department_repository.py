from abc import ABC, abstractmethod

from my_app.domain.entities.department import Department
from my_app.domain.repository_interfaces.base_repository import (
    DBModelType,
    IBaseRepository,
)


class IDepartmentRepository(IBaseRepository[Department, DBModelType], ABC):
    @abstractmethod
    def get_department_for_user(self, user_id: str) -> Department | None:
        raise NotImplementedError()
    
    
    
    