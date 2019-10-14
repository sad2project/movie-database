from utils.domain import Entity, ID

from enum import Enum
from typing import Union, List, Optional


class Format(Enum):
    DVD = 1
    BluRay = 2
    TBD = 3


class MediaID(ID):
    def __init__(self, id):
        super().__init__('MEDIA', id)

    @staticmethod
    def new_media():
        return MediaID(id=None)


class Media(Entity):

    @staticmethod
    def new():
        return Media(id=MediaID.new_media())


class DiscID(ID):
    def __init__(self, id):
        super().__init__('DISC', id)

    @staticmethod
    def new_disc():
        return DiscID(id=None)


class Disc(Entity):
    def __init__(self, *,
            id: DiscID,
            name: str,
            media: List[Media],
            format: Format):
        """
        'Private'! Do not use! Use the static factory methods instead.
        :param id:
        :param name:
        :param media:
        :param format:
        """
        if not media:
            raise TypeError(f'Invalid media for disc: {media}')
        self.media = media
        super().__init__(id)

    @staticmethod
    def new_movie(name: str, media: Media, format: Format):
        """
        Creates a new (no ID yet) Disc with a single piece of Media.
        :param name: Name of the Disc
        :param media: Media stored on the Disc
        :param format: Format of the Disc
        :return: New (object instantiation) new (no ID yet) Disc with a single
        piece of Media
        """
        return Disc(id=DiscID.new_disc(), name=name, media=[media], format=format)

    @staticmethod
    def new_collection(name: str, media: List[Media], format: Format):
        """
        Creates a new (no ID yet) Disc with a collection of Media.
        :param name: Name of the Disc
        :param media: Collection of Media stored on the Disc
        :param format: Format of the Disc
        :return: New (object instantiation) new (no ID yet) Disc with a collection
        of Media.
        """
        return Disc(id=DiscID.new_disc(), name=name, media=media, format=format)

    @staticmethod
    def restore_movie(id: DiscID, name: str, media: Media, format: Format):
        """
        Creates an existing Disc with a single piece of Media.
        :param id: ID of the Disc
        :param name: Name of the Disc
        :param media: Media stored on the Disc
        :param format: Format of the Disc
        :return: New instance of a Disc with an ID and a single piece of Media.
        """
        return Disc(id=id, name=name, media=[media], format=format)

    @staticmethod
    def restore_collection(id: DiscID, name: str, media: List[Media], format: Format):
        """
        Creates an existing Disc with a collection of Media
        :param id: ID of the Disc
        :param name: Name of the Disc
        :param media: Collection of Media stored on the Disc
        :param format: Format of the Disc
        :return: New instance of a Disc with an ID and a collection of Media
        """
        return Disc(id=id, name=name, media=media, format=format)