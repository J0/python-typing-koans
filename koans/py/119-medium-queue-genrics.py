"""
Koan to learn generic declaration
"""
import typing as t
from typing import TypeVar, Generic,  Iterable

T = TypeVar('T')

# Annotate the Queue class as a generic to accept
# any data type but only same data type can be queued


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item: T) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> T:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)


def main() -> None:
    # Annotate the variable as Queue of string
    str_queue: Queue[str] = Queue()
    str_queue.enqueue("welcome")
    # Annotate the variable as Queue of int
    id_queue: Queue[int] = Queue()
    id_queue.enqueue(1)
    id_queue.dequeue()


if __name__ == "__main__":
    main()
