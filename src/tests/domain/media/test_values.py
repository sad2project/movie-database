from domain.media import *
from utils.domain import DomainError

from pytest import raises
from ...helpers import *
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


@properties(disc_num=integers(min_value=1), out_of=integers(min_value=1))
def test_disc_num_cannot_be_greater_than_max(disc_num, out_of):
    with raises(DomainError):
        DiscNumber(disc_num + out_of, out_of)


@properties(max=integers(max_value=1))
def test_disc_num_max_cannot_be_less_than_2(max):
    with raises(DomainError):
        DiscNumber(max - 14, max)


@properties(out_of=integers(min_value=2))
def test_can_access_disc_num_pieces(out_of):
    disc_num = randint(1, out_of)
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
def test_cannot_make_empty_imdb_link():
    with raises(DomainError):
        Imdb("")


def test_can_make_imdb_link():
    Imdb("0417299")


def test_imdb_link_cannot_be_non_digits():
    with raises(DomainError):
        Imdb("054654968t")


def test_imdb_url_generation():
    sut = Imdb("555")

    result = sut.url

    assert result == "https://imdb.com/title/tt555"
