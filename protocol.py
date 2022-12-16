from dataclasses import dataclass, asdict, KW_ONLY
from enum import Enum


class DataTypes(Enum):
    MESSAGE = 'message'
    COORDS = 'coords'
    EMOJI = 'emoji'


@dataclass(frozen=True, slots=True)
class Protocol:
    _: KW_ONLY  # так лучше
    author: str
    data_type: DataTypes  # сообщение, эмодзи, координаты
    text: str = ''
    from_pos: (int, int) = ''
    to_pos: (int, int) = ''
    emoji: str = ''
