import enum
import json
import typing
from typing import Optional, Self


class Method(enum.Enum):
    POST = enum.auto()


class RequestBuilderBase:
    def __init__(self):
        self.url: Optional[str] = None

    def with_url(self, url: str) -> typing.Self:
        self.url = url
        return self


class RequestBuilderWithoutBody(RequestBuilderBase):
    def __init__(self):
        super().__init__()
        self.body: Optional[str] = None

    def body_json(self, data) -> "RequestBuilderWithBody":
        self.body = json.dumps(data)
        return RequestBuilderWithBody(self.url, self.body)

    def body_str(self, data: str) -> "RequestBuilderWithBody":
        self.body = data
        return RequestBuilderWithBody(self.url, self.body)


class Request:
    pass


class RequestBuilderWithBody(RequestBuilderBase):
    def __init__(self, url: Optional[str], body: str):
        super().__init__()
        self.body = body
        self.url = url

    def build(self) -> Request:
        return Request()


builder = (
    RequestBuilderWithoutBody()
        .with_url("http://www.seznam.cz")
        .body_str("asd")
        .with_url("foo")
        .build()
)
