import re

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

    @property
    def next_disc(self):
        """
        :return: the next @DiscNumber in this DiscNumber's collection. If this
        is the last disc in the collection, raises a @DomainError
        """
        return DiscNumber(self.disc_num + 1, self.out_of)

    @classmethod
    def for_collection(cls, size):
        """
        Creates a generator that yields all the DiscNumbers in a collection the
        size of `size`
        :param size: number of discs in the collection
        :return: generator that yields the needed DiscNumbers
        """
        if size < 2:
            raise DomainError(
                "There must be at least 2 discs to constitute the need for a disc number")
        return cls._for_collection(size)

    @classmethod
    def _for_collection(cls, size):
        for i in range(1, size+1):
            yield cls(i, size)

    def __str__(self):
        """
        :return: a string in the format "Disc # of #"
        """
        return self.strformat()

    def __repr__(self):
        """
        :return: a string representation that could potentially be instantiated
        """
        return f'{self.__class__.__name__}({self.disc_num}, {self.out_of})'

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

    def __str__(self):
        return f'IMDB tt{self.id}'

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.id)})'


class Name:
    """
    Wraps a string to represent the name of something.
    """
    def __init__(self, text: str):
        """
        Instantiate a @Name with a string to represent a name. Please only use
        printable characters (as seen in string.printable). Leading and trailing
        whitespace is stripped out. If the resulting string is empty, a
        @DomainError will be raised
        :param text: string to be used as the name
        """
        stripped_text = text.strip()
        if stripped_text == '':
            raise DomainError('Cannot have an empty name')
        self.name = stripped_text

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class EpisodeNumber:
    """
    Wraps an integer to represent an episode number in a television show
    """
    def __init__(self, number):
        if number < 1:
            raise DomainError("Episode Number must be at least 1")
        self.number = number

    def __str__(self):
        return f'episode {self.number}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.number})'


class Slottable:
    """
    @Slottable is just a "tag interface" that labels a class as something that
    can be "inserted" into a binder slot.
    """

    pass
