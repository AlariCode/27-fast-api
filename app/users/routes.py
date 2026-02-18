import logging
from fastapi import APIRouter

from app.users.schema import UserRegisterResponse, UserRegisterRequest, UserLoginRequest, UserLoginResponse
from app.users.service import UserServiceDeps


router = APIRouter(prefix="/v1/auth", tags=["Auth"])
logger = logging.getLogger(__name__)


@router.post("/register", response_model=UserRegisterResponse, status_code=201)
async def register(service: UserServiceDeps, data: UserRegisterRequest):
    res = await service.create(data)
    return UserRegisterResponse(
        id=res.id,
        email=res.email,
    )


@router.post("/login", response_model=UserLoginResponse)
async def login(service: UserServiceDeps, data: UserLoginRequest):
    res = await service.authenticate(data)
    return UserLoginResponse(
        is_loggined=res
    )
