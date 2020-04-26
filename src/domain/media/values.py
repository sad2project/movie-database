from utils.domain import Entity, ID, Value, DomainError, non_empty, is_numeric


class DiscNumber(Value):
    """
    @DiscNumber is used to tell you which disc in a collection of discs that a
    certain disc is, i.e. Disc 1 of 2.
    """

    def __init__(self, disc_num: int, out_of: int):
        if disc_num <= 0:
            raise DomainError("Disc number must be positive")
        if out_of < 2:
            raise DomainError(
                "There must be at least 2 discs to constitute the need for a disc number")
        if disc_num > out_of:
            raise DomainError("Disc number cannot be greater than the total number of discs")
        super().__init__(disc_num, out_of)
        self.disc_num = disc_num
        self.out_of = out_of

    def __str__(self):
        """
        :return: a string in the format "Disc # of #"
        """
        return self.strformat()

    def strformat(self, prefix="Disc ", include_max=True, separator=" of "):
        """
        Returns a formatted string representation of the @DiscNumber
        :param prefix: default = "Disc ". This is a label that goes before the
            numbers
        :param include_max: default = True. Determines whether to include the
            second number, i.e the number after "of"
        :param separator: default = " of ". This is a separator between the two
            numbers. The separator is ignored if include_max is False
        :return: string representation of the @DiscNumber using the given
            formatting options
        """
        if prefix is None:
            prefix = ''
        if include_max:
            return f'{prefix}{self.disc_num}{separator}{self.out_of}'
        else:
            return f'{prefix}{self.disc_num}'


class Imdb:
    """
    @Imdb represents an Imdb id, which can be used to look up information on
    IMDB about the movie/show/episode identified.
    """

    def __init__(self, id: str):
        self.id = is_numeric(non_empty(id))

    @property
    def url(self):
        """
        :return: a url to the identified title's page on IMDB
        """
        return f"https://imdb.com/title/tt{self.id}"


class Slottable:
    """
    @Slottable is just a "tag interface" that labels a class as something that
    can be "inserted" into a binder slot.
    """

    pass
