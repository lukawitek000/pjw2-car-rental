from werkzeug.security import check_password_hash, generate_password_hash
from domain.role import Role
from infrastructure.entities import User


class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, username: str, password: str) -> User:
        if self.__verify_password(username, password):
            return self.user_repository.find_by_username(username)
        return None

    def signup(self, username: str, email: str, password: str, role: Role) -> User:
        password_hash = self.__hash_password(password)
        user = User(username=username, email=email, password_hash=password_hash)
        user.role_enum = role
        self.user_repository.create_user(user)
        return user

    def __hash_password(self, password: str) -> str:
        return generate_password_hash(password)

    def __verify_password(self, username: str, password: str) -> bool:
        user_record = self.user_repository.find_by_username(username)
        if not user_record:
            return False
        return check_password_hash(user_record.password_hash, password)
