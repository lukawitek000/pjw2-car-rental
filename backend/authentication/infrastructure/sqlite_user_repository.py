from authentication.domain.user_repository import UserRepository
from authentication.infrastructure.entities import User


class SqliteUserRepository(UserRepository):

    def create_user(self, user):
        user.save()

    def find_by_username(self, username):
        try:
            return User.get(User.username == username)
        except User.DoesNotExist:
            return None





