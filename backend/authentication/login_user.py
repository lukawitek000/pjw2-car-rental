from flask_login import UserMixin


class LoginUser(UserMixin):
    def __init__(self, username, email, name, role):
        self.username = username
        self.email = email
        self.name = name
        self.role = role

    def get_id(self):
        return self.username

    @staticmethod
    def from_domain_model(user):
        return LoginUser(
            username=user.username,
            email=user.email,
            name=user.name,
            role=user.role
        )