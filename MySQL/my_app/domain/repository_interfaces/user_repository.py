from abc import ABC, abstractmethod

from my_app.domain.entities.user import User
from my_app.domain.repository_interfaces.base_repository import DBModelType, IBaseRepository

class IUserRepository(IBaseRepository[User, DBModelType], ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError()
    
    
    
    