from my_app.domain.entities.user import User
from my_app.domain.repository_interfaces.user_repository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: str):
        return self.user_repository.get_by_id(user_id)

    def get_users(self):
        return self.user_repository.list_all()

    def create_user(self, user: User):
        return self.user_repository.add(user)

    def update_user(self, user: User):
        return self.user_repository.update(user)

    def delete_user(self, user_id: str):
        return self.user_repository.remove(user_id)

