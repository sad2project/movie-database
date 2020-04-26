from hypothesis import given, settings
from hypothesis.strategies import one_of, sampled_from, just, builds, integers, none, text, lists
import pytest

from domain.disc import *
from utils.domain import DomainError


def properties(**kwargs):
    return lambda func: given(**kwargs)(settings(max_examples=10)(func))

################################################################################
# MediaID Tests
################################################################################
@properties(id_num=integers())
def MediaID_has_table_name_MEDIA(id_num):
    id = MediaID(id_num)

    assert id.table_name == 'MEDIA'


@properties(id_num=integers())
def MediaID_has_given_id_number(id_num):
    id = MediaID(id_num)

    assert id.id == id_num


def MediaID_new_id_has_None_id():
    id = MediaID.new_media()

    assert id.id is None

################################################################################
# DiscID Tests
################################################################################
@properties(id_num=integers())
def DiscID_has_table_name_DISC(id_num):
    id = DiscID(id_num)

    assert id.table_name == 'DISC'


@properties(id_num=integers())
def DiscID_has_given_id_number(id_num):
    id = DiscID(id_num)

    assert id.id == id_num


def DiscID_new_id_has_None_id():
    id = DiscID.new_disc()

    assert id.id is None


################################################################################
# Media Tests
################################################################################


################################################################################
# Disc Tests
################################################################################
# Disc Use Cases:
# + Create new disc with movie
# + Create new disc with multiple movies
# + Create new TV Show with multiple discs and movies
# + Create without owning it yet (do this via Media without Discs)
# + Switch it to being owned (based on format)?
# + Insert into a binder slot

id_default = builds(DiscID, integers())
name_default = text(min_size=1)
collection_media_default = lists(just(Media.new()), min_size=1)
movie_media_default = just(Media.new())
format_default = sampled_from(Format)
collection_defaults = {'id': id_default, 'name': name_default,
        'media': collection_media_default, 'format': format_default}
movie_defaults = {'id': id_default, 'name': name_default,
        'media': movie_media_default, 'format': format_default}


@properties(**collection_defaults)
def media_cannot_be_empty(id: DiscID, name: str, format: Format, **kwargs):
    with pytest.raises(DomainError):
        disc = Disc(id, name, [], format)


@properties(**collection_defaults)
def name_cannot_be_empty(id: DiscID, media: List[Media], format: Format, **kwargs):
    with pytest.raises(DomainError):
        disc = Disc(id, "", media, format)


@properties(**collection_defaults)
def can_access_attributes(id: DiscID, name: str, media: List[Media], format: Format):
    disc = Disc(id, name, media, format)

    assert disc.id == id
    assert disc.name == name
    assert disc.media == media
    assert disc.format == format


@properties(**movie_defaults)
def restored_movie_cannot_have_new_id(name: str, media: Media, format: Format, **kwargs):
    with pytest.raises(TypeError):
        disc = Disc.restore_movie(DiscID.new_disc(), name, media, format)


@properties(**movie_defaults)
def restored_movie_otherwise_works(id: DiscID, name: str, media: Media, format: Format):
    disc = Disc.restore_movie(id, name, media, format)

    assert disc.id == id
    assert disc.name == name
    assert disc.media == [media]
    assert disc.strformat == format


@properties(**collection_defaults)
def restored_collection_cannot_have_new_id(name: str, media: List[Media], format:Format, **kwargs):
    with pytest.raises(TypeError):
        disc = Disc.restore_collection(DiscID.new_disc(), name, media, format)


@properties(**collection_defaults)
def restored_collection_otherwise_works(id: DiscID, name: str, media: List[Media], format: Format):
    disc = Disc.restore_collection(id, name, media, format)

    assert disc.id == id
    assert disc.name == name
    assert disc.media == media
    assert disc.strformat == format


@properties(**movie_defaults)
def new_movie_otherwise_works(name: str, media: Media, format:Format, **kwargs):
    disc = Disc.new_movie(name, media, format)

    assert disc.id == DiscID.new_disc()
    assert disc.name == name
    assert disc.media == [media]
    assert disc.strformat == format


@properties(**collection_defaults)
def new_collection_otherwise_works(name: str, media: List[Media], format: Format, **kwargs):
    disc = Disc.new_collection(name, media, format)

    assert disc.id == DiscID.new_disc()
    assert disc.name == name
    assert disc.media == media
    assert disc.strformat == format
