"""
Koan to learn annotating the class variables
"""
import datetime
import random
from string import ascii_letters
from typing import TypedDict, ClassVar, Union, Optional, Type
from random import choice


class UserData(TypedDict):
    name: str
    email: str
    is_active: bool
    last_seen: datetime.datetime


def get_random_user_data() -> UserData:
    generated_string: str = "".join(choice(ascii_letters) for x in range(15))
    return {
        "name": generated_string,
        "email": f"{generated_string}@gmail.com",
        "is_active": random.choice([True, False]),
        "last_seen": datetime.datetime.utcnow(),
    }


class User:
    # Annotate the class variable
    # Documentation: https://docs.python.org/3/library/typing.html#typing.ClassVar
    users: ClassVar[list[User]] = []

    # Annotate the method arguments
    def __init__(self, name: str, email: str, is_active: bool, last_seen: datetime.datetime):
        self.name = name
        self.email = email
        self.is_active = is_active
        self.last_seen = last_seen

    # Annotate the return type
    @classmethod
    def add_user(cls, user: User) -> None:
        cls.users.append(user)

    # Annotate the method to return user when found and return None when missing
    @classmethod
    def get_user(cls, name: str) -> Optional[User]:
        for user in cls.users:
            if user.name == name:
                return user
        return None


# Annotate input arguments and return type as User
def create_user(name: str, email: str, is_active: bool, last_seen: datetime.datetime) -> User:
    return User(name=name, email=email, is_active=is_active, last_seen=last_seen)


def main() -> None:
    for _ in range(10):
        user_data = get_random_user_data()
        user: User = create_user(**user_data)
        User.add_user(user)

    # Annotate the variable
    new_user: Optional[User] = User.get_user(name="Guido")
