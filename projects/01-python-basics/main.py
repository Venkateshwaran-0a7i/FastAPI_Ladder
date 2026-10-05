from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


# 1. Functions with type hints

def add_numbers(a: int, b: int) -> int:
    return a + b


def greet(name: str, age: Optional[int] = None) -> str:
    if age is None:
        return f"Hello, {name}!"
    return f"Hello, {name}! You are {age} years old."


# 2. Class example

@dataclass
class Student:
    name: str
    grade: int

    def summary(self) -> str:
        return f"{self.name} has grade {self.grade}."


# 3. Async example

async def fetch_data(delay: float = 0.1) -> str:
    import asyncio

    await asyncio.sleep(delay)
    return "Data fetched successfully"


# 4. Pydantic example

class UserCreate(BaseModel):
    username: str
    email: str
    age: int


# 5. Practice tasks
if __name__ == "__main__":
    print(add_numbers(10, 20))
    print(greet("Alice", 25))

    student = Student("Sam", 90)
    print(student.summary())

    import asyncio

    print(asyncio.run(fetch_data()))

    user = UserCreate(username="sam123", email="sam@example.com", age=22)
    print(user)
