import dataclasses
from typing import Optional


@dataclasses.dataclass
class ParsedPerson:
    id: int
    age: int


def parse_id_age(text: str) -> Optional[ParsedPerson]:
    items = text.split("-")
    if len(items) != 2:
        return None

    try:
        id = int(items[0])
        age = int(items[1])
        return ParsedPerson(id=id, age=age)
    except ValueError:
        return None


res = parse_id_age("10-16")
if res is not None:
    print(res.age)
