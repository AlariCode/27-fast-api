from pydantic import BaseModel


class UserLoginRequest(BaseModel):
    email: str
    password: str

    model_config = {"extra": "forbid"}


class UserLoginResponse(BaseModel):
    is_loggined: bool


class UserRegisterRequest(BaseModel):
    email: str
    password: str

    model_config = {"extra": "forbid"}


class UserRegisterResponse(BaseModel):
    id: int
    email: str
