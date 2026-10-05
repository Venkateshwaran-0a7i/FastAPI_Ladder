import hashlib
import secrets
from datetime import datetime, timedelta

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Auth and Security Project")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserLogin(BaseModel):
    username: str
    password: str


USERS_DB = {
    "admin": {
        "password_hash": hashlib.sha256("secret123".encode()).hexdigest(),
    }
}


def create_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    return f"token_for_{username}_{secrets.token_hex(8)}"


@app.post("/login")
def login(user: UserLogin) -> dict:
    stored = USERS_DB.get(user.username)
    if not stored:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    password_hash = hashlib.sha256(user.password.encode()).hexdigest()
    if stored["password_hash"] != password_hash:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.username)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/profile")
def get_profile(authorization: str = Header(None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")

    token = authorization.replace("Bearer ", "")
    if "token_for_" not in token:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"message": "Authenticated user profile", "token": token}


# Real production version:
# - use passlib/bcrypt or argon2 for password hashing
# - use PyJWT for signed JWT tokens
# - validate user roles and permissions
# - add file upload endpoint with UploadFile
