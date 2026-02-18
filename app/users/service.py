import logging
from typing import Annotated

from fastapi import Depends, HTTPException

from app.users.model import User
from app.users.repository import UserRepositoryDeps
from app.users.schema import UserLoginRequest, UserRegisterRequest
from app.users.security import hash_password, verify_password


logger = logging.getLogger(__name__)


def get_user_service(
    user_repo: UserRepositoryDeps
):
    return UserService(user_repo)


class UserService:
    def __init__(self, user_repo: UserRepositoryDeps):
        self.user_repo = user_repo

    async def create(self, data: UserRegisterRequest):
        user = await self.user_repo.get_by_email(data.email)
        if user:
            raise HTTPException(400, "User already exist")
        hashed = hash_password(data.password)
        user = User(email=data.email, hashed_password=hashed)
        return await self.user_repo.save(user)

    async def authenticate(self, data: UserLoginRequest):
        user = await self.user_repo.get_by_email(data.email)
        if user is None:
            return False
        if not verify_password(data.password, user.hashed_password):
            return False
        return True


UserServiceDeps = Annotated[UserService, Depends(get_user_service)]
