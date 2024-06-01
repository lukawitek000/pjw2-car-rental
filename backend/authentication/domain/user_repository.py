from abc import ABC, abstractmethod

from authentication.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User, password_hash: str):
        pass

    @abstractmethod
    def find_by_username(self, username) -> User:
        pass

    @abstractmethod
    def find_password_hash(self, username) -> str:
        pass

