from dataclasses import dataclass, asdict


@dataclass(frozen=True, slots=True)
class Protocol:
    text: str
    author: str
