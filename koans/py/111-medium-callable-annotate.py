"""
Koan to learn annotating the callables or functions.
"""

# Annotate the function arguments
# Documentation: https://docs.python.org/3/library/typing.html?highlight=typing#callable
# Documentation: https://docs.python.org/3/library/typing.html?highlight=typing#typing.Iterable

from typing import Callable, Iterable, Dict


def user_sort(data: Iterable[Dict[str, int]], func: Callable[[Dict[str, int]], int]) -> Iterable[Dict[str, int]]:
    return sorted(data, key=func)


def key_func(item: Dict[str, int]) -> int:
    return item["user_id"]


def main() -> None:
    # Annotate the data
    data: Iterable[Dict[str, int]] = [
        {"user_id": 1, "is_active": True},
        {"user_id": 34, "is_active": True},
        {"user_id": 3, "is_active": False},
    ]

    assert user_sort(data, key_func)


if __name__ == "__main__":
    main()
