from hypothesis import assume
from hypothesis.strategies import composite, text, integers, one_of, none
import string

from media.values import *
from media.media_types import *


@composite
def disc_numbers_strategy(draw):
    first = draw(integers(min_value=1))
    second = draw(integers(min_value=max(first, 2)))
    return first, second

@composite
def disc_number_strategy(draw, numbers_strategy=disc_numbers_strategy):
    return DiscNumber(*draw(numbers_strategy))

def imdb_link_strategy():
    return text(alphabet='0123456789', min_size=1, max_size=30)

@composite
def imdb_strategy(draw, id_strategy=text(alphabet='0123456789', min_size=1, max_size=30)):
    return Imdb(draw(id_strategy))

def name_value_strategy():
    return text(min_size=1, alphabet=string.printable)

@composite
def name_strategy(draw, value_strategy=name_value_strategy()):
    value: str = draw(value_strategy)
    assume(value.strip() != '')
    return Name(value)

def episode_number_value_strategy():
    return integers(min_value=1)

@composite
def episode_number_strategy(draw, number_strategy=episode_number_value_strategy):
    return EpisodeNumber(draw(number_strategy))

@composite
def media_id_strategy(draw, id_strategy=one_of(none(), integers(min_value=1))):
    return MediaID(draw(id_strategy))

@composite
def movie_strategy(draw,
                   media_id_strategy=media_id_strategy,
                   name_strategy=name_strategy,
                   imdb_strategy=imdb_strategy):
    return Movie(draw(media_id_strategy), draw(name_strategy), draw(imdb_strategy))