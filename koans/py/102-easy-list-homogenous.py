"""
Koan to learn annotating the Python list data type
"""
from typing import Any, List

# Annotate list of integers
# Documentation: https://docs.python.org/3/library/typing.html#typing.List
nos: List[int] = [1, 2, 23, 45]
result: int = sum(nos)

# Annotate list of list of integers
matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6]]
