"""
Koan to learn annotating the class
"""
import datetime
import random
from string import ascii_letters
from typing import TypedDict, List, ClassVar


# Annotate the user data to fit the get_random_user_data
class UserData(TypedDict):
    name: ClassVar[str]
    email: ClassVar[str]
    is_active: ClassVar[bool]
    last_seen: ClassVar[datetime.datetime]


def get_random_user_data() -> UserData:
    generated_string: str = "".join(
        random.choice(ascii_letters) for x in range(15))
    return {
        "name": generated_string,
        "email": f"{generated_string}@gmail.com",
        "is_active": random.choice([True, False]),
        "last_seen": datetime.datetime.utcnow(),
    }


class User:
    # Annotate the method arguments
    def __init__(self, name: str, email: str, is_active: bool, last_seen: datetime.datetime):
        self.name = name
        self.email = email
        self.is_active = is_active
        self.last_seen = last_seen


# Annotate input arguments and return type as User
def create_user(name: str, email: str, is_active: bool, last_seen: datetime.datetime) -> User:
    return User(name=name, email=email, is_active=is_active, last_seen=last_seen)


def main() -> None:
    # Annotate list of users
    users: List[User] = []
    for _ in range(10):
        user_data: UserData = get_random_user_data()
        user: User = create_user(**user_data)
        users.append(user)
