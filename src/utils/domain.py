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

    def __str__(self):
        return f'{self.table_name} ID {self.id}'
