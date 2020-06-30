from media import *
from tests.media.type_builders import disc_numbers_strategy, imdb_link_strategy, \
    episode_number_value_strategy, name_value_strategy
from utils.domain import DomainError

from pytest import raises
from tests.helpers import *
from random import randint
from re import compile, search
import string

integers = strat.integers


# DiscNumber
################################################################################
@properties(disc_num=integers(max_value=0))
def test_disc_num_cannot_be_less_than_1(disc_num):
    with raises(DomainError):
        DiscNumber(disc_num, 2)


@strat.composite
def reversed_disc_nums(draw):
    second = draw(integers(min_value=1))
    first = draw(integers(min_value=second+1))
    return first, second

@properties(nums=reversed_disc_nums())
def test_disc_num_cannot_be_greater_than_max(nums):
    disc_num, out_of = nums
    with raises(DomainError):
        DiscNumber(disc_num, out_of)


@properties(max=integers(max_value=1))
def test_disc_num_max_cannot_be_less_than_2(max):
    with raises(DomainError):
        DiscNumber(max, max)


@properties(nums=disc_numbers_strategy())
def test_can_access_disc_num_pieces(nums):
    disc_num, out_of = nums
    sut = DiscNumber(disc_num, out_of)

    assert sut.disc_num == disc_num
    assert sut.out_of == out_of
    assert sut._pieces == (disc_num, out_of)


def test_next_disc():
    sut = DiscNumber(1, 4)

    result = sut.next_disc

    assert result == DiscNumber(2, 4)

    result = result.next_disc

    assert result == DiscNumber(3, 4)

    result = result.next_disc

    assert result == DiscNumber(4, 4)

    with raises(DomainError):
        result.next_disc


@properties(out_of=integers(min_value=2, max_value=50))
def test_discs(out_of):
    sut = DiscNumber.for_collection(out_of)

    for i in range(1, out_of+1):
        assert next(sut) == DiscNumber(i, out_of)

    with raises(StopIteration):
        next(sut)


@properties(out_of=integers(max_value=1))
def test_discs_must_be_at_least_2(out_of):
    with raises(DomainError):
        sut = DiscNumber.for_collection(out_of)


def test_disc_num_str():
    sut = DiscNumber(1, 2)

    result = str(sut)

    assert result == 'Disc 1 of 2'


def test_disc_num_str_format_defaults_to_str():
    sut = DiscNumber(2, 3)

    assert str(sut) == sut.strformat()


def test_disc_num_str_format_prefix():
    sut = DiscNumber(3, 4)

    assert sut.strformat(prefix='cow ') == 'cow 3 of 4'


def test_disc_num_str_format_none_prefix():
    sut = DiscNumber(4, 5)

    assert sut.strformat(prefix=None) == '4 of 5'


def test_disc_num_str_format_separator():
    sut = DiscNumber(6, 7)

    assert sut.strformat(separator='/') == 'Disc 6/7'


def test_disc_num_str_format_include_max():
    sut = DiscNumber(7, 8)

    assert sut.strformat(include_max=False) == 'Disc 7'


def test_disc_num_str_format_mix():
    sut = DiscNumber(5, 9)

    assert sut.strformat(prefix=None, separator=" of the ") == '5 of the 9'


def test_disc_num_repr():
    sut = DiscNumber(7, 9)

    assert repr(sut) == "DiscNumber(7, 9)"


# IMDB
################################################################################
non_digits_pattern = compile(r'\D')


def has_non_digits(string):
    return search(non_digits_pattern, string) is not None


def test_cannot_make_empty_imdb():
    with raises(DomainError):
        Imdb("")


@properties(id=imdb_link_strategy())
def test_can_make_imdb(id):
    Imdb(id)


@properties(id=strat.text(min_size=1, max_size=30))
def test_imdb_cannot_have_non_digits(id: str):
    assume(has_non_digits(id))

    with raises(DomainError):
        Imdb("054654968t")


@properties(id=imdb_link_strategy())
def test_imdb_url_generation(id):
    sut = Imdb(id)

    result = sut.url

    assert result == f'https://imdb.com/title/tt{id}'


@properties(id=imdb_link_strategy())
def test_imdb_string(id):
    sut = Imdb(id)

    assert str(sut) == f'IMDB tt{id}'


@properties(id=imdb_link_strategy())
def test_imdb_repr(id):
    sut = Imdb(id)

    assert repr(sut) == f"Imdb('{id}')"


# Name
################################################################################
@properties(text=name_value_strategy())
def test_can_make_name(text):
    assume(text.strip() != '')
    sut = Name(text)


def test_name_cannot_be_empty():
    with raises(DomainError):
        sut = Name('')


@properties(text=strat.text(alphabet=string.whitespace))
def test_name_cannot_be_only_whitespace(text):
    with raises(DomainError):
        sut = Name(text)


# EpisodeNumber
################################################################################
@properties(number=episode_number_value_strategy())
def test_can_make_episode_number(number):
    sut = EpisodeNumber(number)


@properties(number=strat.integers(max_value=0))
def test_episode_number_cannot_be_lower_than_1(number):
    with raises(DomainError):
        sut = EpisodeNumber(number)


@properties(number=episode_number_value_strategy())
def test_episode_number_has_attributes(number):
    sut = EpisodeNumber(number)

    assert sut.number == number


@properties(number=episode_number_value_strategy())
def test_episode_number_string(number):
    sut = EpisodeNumber(number)

    assert str(sut) == f'episode {number}'


@properties(number=episode_number_value_strategy())
def test_episode_number_repr(number):
    sut = EpisodeNumber(number)

    assert repr(sut) == f'EpisodeNumber({number})'
