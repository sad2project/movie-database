from .values import *
from utils.domain import Entity, ID, non_empty


class MediaID(ID):
    def __init__(self, id):
        super().__init__("MEDIA", id)

    @classmethod
    def new(cls):
        return MediaID(None)


class Movie(Entity, Slottable):
    def __init__(self, id: MediaID, name: Name, imdb: Imdb):
        super().__init__(id)
        self.name = name
        self.imdb = imdb


class Episode(Entity):
    def __init__(self, id: MediaID, number: EpisodeNumber, imdb: Imdb):
        pass


# Movie (id, name, imdb) Slottable!
# Episode (id, number, name, imdb)
# Season (id, number, name, episode list)
# Show (id, name, season list, imdb)
# Series (id, name, movie list)
