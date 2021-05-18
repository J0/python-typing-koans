"""
Koan to learn annotating the Python dictionary
"""
from collections import defaultdict

from typing import Dict

# Annotate the dictionary
# Documentation: https://docs.python.org/3/library/typing.html#typing.Dict
result: Dict[str, int] = defaultdict(int)
words = ["welcome", "to", "the", "world",
         "world", "is", "an", "uneven", "place"]
for word in words:
    result[word] += 1

print(result)
