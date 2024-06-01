from authentication.domain.user import User
from authentication.domain.user_repository import UserRepository
from authentication.infrastructure.user_entity import UserEntity
from database import database


class SqliteUserRepository(UserRepository):

    def create_user(self, user: User, password_hash: str):
        try:
            user_entity = UserEntity.from_domain_model(user, password_hash)
            saved = user_entity.save(force_insert=True)
            if saved == 0:
                raise Exception("Error creating user")
        except Exception as e:
            print(f"Error creating user: {e}")

    def find_by_username(self, username) -> User:
        try:
            return UserEntity.get(UserEntity.username == username).to_domain_model()
        except UserEntity.DoesNotExist:
            return None

    def find_password_hash(self, username) -> str:
        try:
            return UserEntity.get(UserEntity.username == username).password_hash
        except UserEntity.DoesNotExist:
            return None





