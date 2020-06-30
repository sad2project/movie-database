from media import *

from tests.helpers import *
from tests.media.type_builders import *
import string


# Movie
################################################################################
@properties(id=media_id_strategy(), name=name_strategy(), imdb=imdb_strategy())
def test_can_create_movie(id, name, imdb):
    Movie(id, name, imdb)


@properties(id=media_id_strategy(), name=name_strategy(), imdb=imdb_strategy())
def test_movie_has_all_attributes(id, name, imdb):
    sut = Movie(id, name, imdb)

    assert sut.id == id
    assert sut.name == name
    assert sut.imdb == imdb


# Episode
################################################################################
