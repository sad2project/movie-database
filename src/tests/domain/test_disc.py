from domain.disc import *

# Disc Use Cases:
# + Create new disc with movie
# + Create new disc with multiple movies
# + Create new TV Show with multiple discs and movies
# + Create without owning it yet
# + Switch it to being owned (based on format)?
# + Insert into a binder slot


def test_cannot_create_disc_without_media():
    try:
        disc = Disc(id=DiscID.new_disc(), media=[], name='Test Disc', format=Format.TBD)
        assert False
    except TypeError as e:
        assert 'Invalid media' in str(e)


def test_can_access_id():
    disc = Disc.restore_movie(id=DiscID(1), name='Test Disc', media=Media.new(), format=Format.TBD)

    assert disc.id == DiscID(1)


def test_that():
    pass
