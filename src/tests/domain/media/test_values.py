from domain.media import *
from utils.domain import DomainError

from pytest import raises
from ...helpers import *
integers = strategies.integers
from random import randint


#DiscNumber
################################################################################
@properties(disc_num=integers())
def test_disc_num_cannot_be_less_than_1(disc_num):
    assume(disc_num < 1)
    with raises(DomainError):
        DiscNumber(disc_num, 2)


@properties(disc_num=integers(), out_of=integers())
def test_disc_num_cannot_be_greater_than_max(disc_num, out_of):
    assume(out_of >= 2)
    assume(disc_num > 0)
    with raises(DomainError):
        DiscNumber(disc_num + out_of, out_of)


@properties(max=integers())
def test_disc_num_max_cannot_be_less_than_2(max):
    assume(max < 2)
    with raises(DomainError):
        DiscNumber(max - 14, max)


@properties(out_of=integers())
def test_can_access_disc_num_pieces(out_of):
    assume(out_of >= 2)
    disc_num = randint(1, out_of)
    sut = DiscNumber(disc_num, out_of)

    assert sut.disc_num == disc_num
    assert sut.out_of == out_of
    assert sut._pieces == (disc_num, out_of)


def test_disc_num_str():
    sut = DiscNumber(1, 2)

    result = str(sut)

    assert result == 'Disc 1 of 2'


def test_disc_num_str_format_defaults_to_str():
    sut = DiscNumber(1, 2)

    assert str(sut) == sut.strformat()


def test_disc_num_str_format_prefix():
    sut = DiscNumber(1,2)

    assert sut.strformat(prefix='cow ') == 'cow 1 of 2'


def test_disc_num_str_format_none_prefix():
    sut = DiscNumber(1, 2)

    assert sut.strformat(prefix=None) == '1 of 2'


def test_disc_num_str_format_separator():
    sut = DiscNumber(1, 2)

    assert sut.strformat(separator='/') == 'Disc 1/2'


def test_disc_num_str_format_include_max():
    sut = DiscNumber(1, 2)

    assert sut.strformat(include_max=False) == 'Disc 1'


def test_disc_num_str_format_mix():
    sut = DiscNumber(1, 2)

    assert sut.strformat(prefix=None, separator=" of the ") == '1 of the 2'


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
