from dataclasses import dataclass, asdict


@dataclass(frozen=True, slots=True)
class Protocol:
    author: str
    text: str
    emoji: str
