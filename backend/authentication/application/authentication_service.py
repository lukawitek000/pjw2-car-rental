from werkzeug.security import check_password_hash, generate_password_hash
from authentication.domain.user import User


class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, username, password) -> User:
        if self.__verify_password(username, password):
            return self.user_repository.find_by_username(username)
        return None

    def signup(self, user, password) -> User:
        password_hash = self.__hash_password(password)
        self.user_repository.create_user(user, password_hash)
        return user

    def __hash_password(self, password: str) -> str:
        return generate_password_hash(password)

    def __verify_password(self, username: str, password: str) -> bool:
        password_hash = self.user_repository.find_password_hash(username)
        if not password_hash:
            raise Exception("User not found")
        return check_password_hash(password_hash, password)
