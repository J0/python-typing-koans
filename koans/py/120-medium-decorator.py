"""
Koan to learn annotating the decorator
"""
import typing as t

# annotate the dict to store only ints
cached_results:t.Dict[int,int] = {}

# Annotate the function to receive the function and return the function
# Callable type; Callable[[int], str] is a function of (int) -> str.

def cache(f: t.Callable[[int], int] )-> t.Callable[[int], int]:
    def inner(n:int)->int:
        if n in cached_results:
            return cached_results[n]
        cached_results[n] = f(n)
        return cached_results[n]

    return inner


@cache
def factorial(n: int)->int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
