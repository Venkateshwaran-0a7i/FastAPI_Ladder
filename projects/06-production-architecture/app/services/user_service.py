from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserOut


class UserService:
    _db: list[User] = []

    @classmethod
    def get_users(cls) -> list[UserOut]:
        return [UserOut(id=user.id, name=user.name, email=user.email) for user in cls._db]

    @classmethod
    def create_user(cls, payload: UserCreate) -> UserOut:
        user = User(id=len(cls._db) + 1, name=payload.name, email=payload.email)
        cls._db.append(user)
        return UserOut(id=user.id, name=user.name, email=user.email)
