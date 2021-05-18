"""
Koan to learn annotating the dictionary with fixed key/values.
"""

import datetime
import random
from typing import TypedDict
from uuid import UUID


# Annotate the return type as TypedDict
# Documentation: https://docs.python.org/3/library/typing.html#typing.TypedDict

class User(TypedDict):
    user_id: UUID
    company_id: int
    is_active: bool
    last_seen: datetime.datetime


def get_random_user_data() -> User:
    return {
        "user_id": UUID(),
        "company_id": random.randint(1, 1_000_000),
        "is_active": random.choice([True, False]),
        "last_seen": datetime.datetime.utcnow(),
    }


print(get_random_user_data())
