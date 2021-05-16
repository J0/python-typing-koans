"""
Koan to learn annotating the Python tuple
"""
from typing import Any, Tuple

# result is annotated as Any, annotate it as tuple
# How to annotate tuple: https://docs.python.org/3/library/typing.html#typing.Tuple
result: Tuple[str, str, int] = ("stdin", "stdout", 2)

# annotate the variable as tuple of integers
values: Tuple[int, ...] = tuple(range(10))
