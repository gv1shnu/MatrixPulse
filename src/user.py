# Third party library
from flask_login import UserMixin

# Internal imports
from src.handler import handler


class User(UserMixin):
    def __init__(
            self,
            id_,
            name,
            email,
            profile_pic
    ):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        user = handler.get_user(user_id)
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1],
            email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def create(
            id_,
            name,
            email,
            profile_pic
    ):
        handler.insert_user(
            (id_, name, email, profile_pic)
        )
