from utils.domain import Entity, ID

from enum import Enum
from typing import Union, List


class Format(Enum):
    DVD = 1
    BluRay = 2
    TBD = 3


class Media(Entity):
    pass


class Disc(Entity):
    def __init__(self, *,
            name: str,
            media: Union[Media, List[Media]],
            format: Format,
            id:ID =None):
        if not media:
            raise TypeError(f'Invalid media for disc: {media}')7♣
        super().__init__(id)