from fastapi_users import models


class User(models.BaseUser):
    name: str
    is_seller: bool


class UserCreate(User, models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
