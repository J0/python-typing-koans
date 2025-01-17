"""
Koan to learn type of class when passed as an argument.
"""

import json
from typing import Any, Type, Union

# Figure out how to ignore Any Error
JSONData = dict[str, Any]  # type: ignore


class JSONResponse:
    def __init__(self, data: JSONData):
        self.data = data

    # Annotate the return type
    def make_response(self) -> bytes:
        return json.dumps(self.data).encode("utf-8")


# Annotate the return type as the type of response class
# Documentation: https://docs.python.org/3/library/typing.html?highlight=typing#typing.Type
def make_response(resp_klass: Type[JSONResponse], data: JSONData) -> bytes:
    return JSONResponse(data).make_response()


def main() -> None:
    data = {"planet": "Earth"}
    make_response(JSONResponse, data)


if __name__ == "__main__":
    main()
