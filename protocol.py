import dataclasses
from dataclasses import dataclass, asdict


@dataclass(frozen=True, slots=True)
class Protocol:
    _: dataclasses.KW_ONLY
    # обязательные
    text: str
    author: str
    # пох
    where_from_pos: (int, int) = (0, 0)
    where_to_pos: (int, int) = (0, 0)
    type: str = '' # тип тож обязательным сделаем


