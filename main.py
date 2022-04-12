from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from core.db import database
from routes import routes
from user.users import auth_backends, get_user_manager
from user.schemas import User, UserCreate, UserUpdate, UserDB

app = FastAPI()

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backends],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(routes)
app.include_router(
    fastapi_users.get_auth_router(auth_backends),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)
