from domain.media import Movie, Disc, Format


def test_movie_has_attributes():
    disc = Disc("Title", Format.DVD)
    movie = Movie("Title", imdb=4154796, disc=disc)

    assert movie.title == "Title"
    assert movie.imdb_code == 4154796
    assert movie.disc == disc


def test_movie_no_disc_is_not_owned():
    movie = Movie("Title", imdb=1)

    assert not movie.is_owned


def test_movie_has_disc_is_owned():
    movie = Movie("Title", imdb=2, disc=Disc("Title", Format.DVD))

    assert movie.is_owned


def test_disc_has_attributes():
    disc = Disc("Title", Format.DVD)

    assert disc.title == "Title"
    assert disc.format == Format.DVD
