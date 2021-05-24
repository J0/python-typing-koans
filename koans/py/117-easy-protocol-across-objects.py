"""
Koan to learn understanding protocol
"""
import typing as t
from io import TextIOWrapper


class SupportsClose(t.Protocol):
    def close(self) -> None:
        ...


class FileWrapper:
    def __init__(self, file: t.TextIO, buffer_size: int = 8192) -> None:
        self.file = file
        self.buffer_size = buffer_size

    def close(self) -> None:
        if hasattr(self.file, "close"):
            self.file.close()


# implement the protocol which has close method and annotate the files variable
def close(files: t.Iterable[SupportsClose]) -> None:
    for f in files:
        f.close()


def main() -> None:
    close(files=[open("README.md"), FileWrapper(file=open("README.md"))])


if __name__ == "__main__":
    main()
