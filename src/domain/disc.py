from utils.domain import Entity, ID

from enum import Enum
from typing import Union, List, Optional


class Format(Enum):
    DVD = 1
    BluRay = 2
    TBD = 3


class Media(Entity):
    pass


class Disc(Entity):
    def __init__(self, *,
            id: Optional[ID],
            name: str,
            media: List[Media],
            format: Format):
        if not media:
            raise TypeError(f'Invalid media for disc: {media}')
        self.media = media
        super().__init__(id)

    @staticmethod
    def new_movie(name: str, media: Media, format: Format):
        return Disc(id=None, name=name, media=[media], format=format)

    @staticmethod
    def new_collection(name: str, media: List[Media], format: Format):
        return Disc(id=None, name=name, media=media, format=format)

    @staticmethod
    def restore_movie(id: ID, name: str, media: Media, format: Format):
        return Disc(id=id, name=name, media=[media], format=format)

    @staticmethod
    def restore_collection(id: ID, name: str, media: List[Media], format: Format):
        return Disc(id=id, name=name, media=media, format=format)
