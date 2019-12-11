class Value:
    def __init__(self, *args):
        self._pieces = args

    def __eq__(self, other):
        return (type(self) == type(other) and
            self._pieces == other._pieces)

    def __hash__(self):
        return hash(self._pieces)

    def __str__(self):
        return f'{type(self).__name__}{self._pieces}'

    __repr__ = __str__


class Entity:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return (type(self) == type(other) and
                self.id == other.id)

    __hash__ = None

    def __str__(self):
        return f'{type(self).__name__}(id={self.id})'


class ID(Value):
    def __init__(self, table_name, id, *args):
        super().__init__(table_name, id, *args)

    @property
    def table_name(self):
        return self._pieces[0]

    @property
    def id(self):
        return self._pieces[1]

    def require_not_new(self):
        if self.id is None:
            raise TypeError('ID is not initialized as required')
        return self

    def is_new(self):
        return self.id is None

    def __str__(self):
        return f'{self.table_name} ID {self.id}'


def non_empty(value):
    """
    Tests that the given collection has a non-zero length. If empty, it raises a
    :TypeError. If it passes, the given collection is returned in order to be
    passed into the variable or into another test such as this one.
    :param value: value to be tested
    :return: given value
    """
    if len(value) == 0:
        raise TypeError('collection is empty; some values are required')
    return value