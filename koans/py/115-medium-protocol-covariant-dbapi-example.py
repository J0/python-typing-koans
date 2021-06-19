"""
Koan to understanding working of Protocol and class inheritance return types
"""
from __future__ import annotations
from typing import Generic, Optional, Protocol, Sequence, Tuple, TypeVar, Union

# PEP249 defines how dbapi structure - https://www.python.org/dev/peps/pep-0249
# The code here is a simplified version of dbapi implementation

# For practical purpose row can hold only a few data types

Value = Union[str, int, float]
Row = Tuple[Value]

# Use covariant to represent CursorT
TCursor = TypeVar('TCursor', bound="Cursor", covariant=True)


# Use Protocol to represent PostgresConnection and MySQLConnect
class Connection(Protocol):
    # Annotate to return MySQLCursor
    def cursor(self) -> Cursor:
        ...

    # Annotate to return a cursor
    def execute(self, sql: str, *params: Sequence[Value])-> Cursor:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...

    def close(self) -> None:
        ...

class Cursor:
    pass

class PostgresConnection:
    def __init__(
        self,
        connstring: str,
        autocommit: bool = False,
        encoding: str = "utf-16le",
        ansi: bool = False,
        readonly: bool = False,
        timeout: int = 10,
    ):
        self.connstring = connstring
        self.autocommit = autocommit
        self.encoding = encoding
        self.ansi = ansi
        self.readonly = readonly
        self.timeout = timeout

    # Annotate to return PostgresCursor
    def cursor(self) -> PostgresCursor:
        return PostgresCursor()

    # Annotate to return a Postgrescursor
    def execute(self, sql: str, *params: Sequence[Value])-> PostgresCursor:
        return PostgresCursor()

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...

    def close(self) -> None:
        ...


class PostgresCursor(Cursor):
    def close(self) -> None:
        ...

    def execute(self, operation: str, parameters: Sequence[Value]) -> Row:
        ...

    def executemany(self, operation: str, parameters: Sequence[Value]) -> Sequence[Row]:
        ...

    def fetchone(self) -> Optional[Row]:
        ...

    def fetchmany(self, size: int = ...) -> Sequence[Row]:
        ...

    def fetchall(self) -> Sequence[Row]:
        ...


class MySQLConnection:
    def __init__(
        self,
        connstring: str,
        autocommit: bool = False,
        encoding: str = "utf-16le",
        ansi: bool = False,
        readonly: bool = False,
        timeout: int = 10,
    ):
        self.connstring = connstring
        self.autocommit = autocommit
        self.encoding = encoding
        self.ansi = ansi
        self.readonly = readonly
        self.timeout = timeout

    # Annotate to return MySQLCursor
    def cursor(self) ->MySQLCursor:
        ...

    # Annotate to return a cursor
    def execute(self, sql: str, *params: Sequence[Value])-> MySQLCursor:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...

    def close(self) -> None:
        ...


class MySQLCursor(Cursor):
    def close(self) -> None:
        ...

    def execute(self, operation: str, parameters: Sequence[Value]) -> Row:
        ...

    def executemany(self, operation: str, parameters: Sequence[Value]) -> Sequence[Row]:
        ...

    def fetchone(self) -> Optional[Row]:
        ...

    def fetchmany(self, size: int = ...) -> Sequence[Row]:
        ...

    def fetchall(self) -> Sequence[Row]:
        ...


# Annotate to return any connection
# Don't use Union Type
def connect(
    connstring: str,
    autocommit: bool = False,
    encoding: str = "utf-16le",
    ansi: bool = False,
    readonly: bool = False,
    timeout: int = 10,
)-> Connection:
    if connstring.startswith("mysql"):
        return MySQLConnection(
            connstring,
            autocommit=autocommit,
            encoding=encoding,
            ansi=ansi,
            readonly=readonly,
            timeout=timeout,
        )
    elif connstring.startswith("psql"):
        return PostgresConnection(
            connstring,
            autocommit=autocommit,
            encoding=encoding,
            ansi=ansi,
            readonly=readonly,
            timeout=timeout,
        )
    raise NotImplementedError(f"{connstring} implementation is not implementated")


def main() -> None:
    connect("mysql://username:password@localhost:3306/db")
    connect("psql://username:password@localhost:5432/db")


if __name__ == "__main__":
    main()
