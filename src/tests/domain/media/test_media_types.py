from domain.media import *
from utils.domain import DomainError

from pytest import raises
from ...helpers import *



# Movie
################################################################################
def test_movie_cannot_have_empty_name():
    with raises(DomainError):
        Movie(MediaID.new(), '', Imdb('22'))


properties(id=strat.one_of(strat.none, strat.integers), imdb=strat.integers())
def test_can_create_movie():
    Movie(MediaID.new(), 'Test Movie', Imdb('22'))


def test_movie_has_all_attributes():
    id = MediaID.new()

    sut = Movie