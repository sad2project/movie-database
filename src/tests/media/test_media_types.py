from media import *

from tests.helpers import *
from .test_values import legal_imdb_link
import string


legal_id = strat.builds(MediaID,
                        strat.one_of(strat.none(), strat.integers(min_value=1)))
legal_imdb = strat.builds(Imdb, legal_imdb_link)
legal_name = strat.builds(Name, strat.text(min_size=1, alphabet=string.printable))


# Movie
################################################################################
@properties(id=legal_id, name=legal_name, imdb=legal_imdb)
def test_can_create_movie(id, name, imdb):
    assume(name.name != '')
    Movie(id, name, imdb)


@properties(id=legal_id, name=legal_name, imdb=legal_imdb)
def test_movie_has_all_attributes(id, name, imdb):
    sut = Movie(id, name, imdb)

    assert sut.id == id
    assert sut.name == name
    assert sut.imdb == imdb


# Episode
################################################################################
