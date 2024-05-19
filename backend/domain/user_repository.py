from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def find_by_username(self, username):
        pass

    @abstractmethod
    def find_by_id(self, user_id):
        pass
