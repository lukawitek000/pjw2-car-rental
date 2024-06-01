from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, username, email, name, role):
        self.username = username
        self.email = email
        self.name = name
        self.role = role

    def get_id(self):
        return self.username
