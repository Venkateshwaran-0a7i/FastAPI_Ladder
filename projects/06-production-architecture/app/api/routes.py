from fastapi import APIRouter

from app.schemas.user_schema import UserCreate, UserOut
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserOut])
def list_users() -> list[UserOut]:
    return UserService.get_users()


@router.post("/", response_model=UserOut, status_code=201)
def create_user(user: UserCreate) -> UserOut:
    return UserService.create_user(user)
