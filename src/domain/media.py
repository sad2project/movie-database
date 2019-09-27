from enum import Enum


class Format(Enum):
    DVD = 1
    BluRay = 2


class Disc:
    # noinspection PyShadowingBuiltins
    def __init__(self,
                 title,
                 format: Format):
        self.title = title
        self.format = format


class Movie:
    def __init__(self,
                 title: str, *,
                 imdb: int,
                 disc: Disc = None):
        self.title = title
        self.imdb_code = imdb
        self.disc = disc

    @property
    def is_owned(self):
        return self.disc is not None
