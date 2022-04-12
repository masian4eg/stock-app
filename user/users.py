from fastapi import Depends
from fastapi_users import BaseUserManager
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from starlette.requests import Request

from core.db import async_session_maker
from .schemas import UserDB, UserCreate

SECRET = 'fg34tg3g3'


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: UserDB, request: Request = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserDB, token: str, request: Request = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserDB, token: str, request: Request = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(async_session_maker)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="users/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backends = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
