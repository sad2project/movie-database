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
        disc = Disc(media=None, name='Test Disc', format=Format.TBD)
        assert False
    except TypeError as e:
        pass


def test():
    pass
