from domain.user_repository import UserRepository
from infrastructure.entities import User


class SqliteUserRepository(UserRepository):

    def create_user(self, user):
        user.save()

    def find_by_username(self, username):
        try:
            return User.get(User.username == username)
        except User.DoesNotExist:
            return None

    def find_by_id(self, user_id):
        try:
            return User.get(User.id == user_id)
        except User.DoesNotExist:
            return None




