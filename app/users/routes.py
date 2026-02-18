import logging
from fastapi import APIRouter, HTTPException

from app.users.schema import JWTResponse, UserRegisterRequest, UserLoginRequest
from app.users.service import UserServiceDeps


router = APIRouter(prefix="/v1/auth", tags=["Auth"])
logger = logging.getLogger(__name__)


@router.post("/register", response_model=JWTResponse, status_code=201)
async def register(service: UserServiceDeps, data: UserRegisterRequest):
    token = await service.create(data)
    return JWTResponse(
        token=token
    )


@router.post("/login", response_model=JWTResponse)
async def login(service: UserServiceDeps, data: UserLoginRequest):
    token = await service.authenticate(data)
    if token is None:
        raise HTTPException(401, "Wrong email or password")
    return JWTResponse(
        token=token
    )
