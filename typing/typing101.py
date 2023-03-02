import typing

from beartype import beartype


# int, str, bool, float
# Optional
# List, Dict, Tuple
# Tuple[int, ...]
# Union
# Generics
# Literal
# Class
# type hinting in strings
# Callable
# Iterable
# Protocol
# Class variables
# Type alias
# New type
# Any


def add(x: int, y: int) -> int:
    return x + y


IntOrString = typing.Union[int, str]

T = typing.TypeVar("T", bound=IntOrString)


def add_same(x: T, y: T) -> typing.List[T]:
    return [x, y]


@beartype
def dynamically_checked(x: int):
    pass


dynamically_checked("asd")
