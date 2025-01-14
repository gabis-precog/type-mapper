from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional


@dataclass(frozen=True)
class SampleSubModel:
    a_value: str

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__


@dataclass(frozen=True)
class SampleModelTyping:
    simple_value: str
    another_value: Dict[str, str]
    more_values: List[int]
    yet_another_value: int
    ml_model: str
    sub_model: Optional[SampleSubModel] = None
    decimal: Optional[float] = None
    created_at: Optional[datetime] = None
    delta: Optional[timedelta] = None

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__


class SampleEnum(Enum):
    item = 'Item'


class SampleOtherEnum(Enum):
    item = '1'
    other = '2'
