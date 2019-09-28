from utils.domain import *


class ValueDouble(Value):
    def __init__(self, foo, bar):
        super().__init__(foo, bar)

    @property
    def foo(self):
        return self._pieces[0]

    @property
    def bar(self):
        return self._pieces[1]


class EntityDouble(Entity):
    def __init__(self, id, foo):
        super().__init__(id)
        self.foo = foo


class IdDouble(ID):
    def __init__(self, id):
        super().__init__("TABLE", id)


def test_value_equals():
    a = ValueDouble(1, 2)
    b = ValueDouble(1, 2)

    assert a == b


def test_value_not_equal():
    a = ValueDouble(1, 2)
    b = ValueDouble(2, 3)

    assert a != b


def test_value_equal_hash():
    a = ValueDouble(1, 2)
    b = ValueDouble(1, 2)

    assert hash(a) == hash(b)


def test_value_inequal_hash():
    a = ValueDouble(1, 2)
    b = ValueDouble(2, 3)

    assert hash(a) != hash(b)


def test_value_string():
    a = ValueDouble(1, 2)

    assert str(a) == "ValueDouble(1, 2)"


def test_value_repr():
    a = ValueDouble(1, 2)

    assert str(a) == repr(a)


def test_value_get_foo():
    a = ValueDouble(1, 2)

    assert a.foo == 1


def test_value_get_bar():
    a = ValueDouble(1, 2)

    assert a.bar == 2
    
    
def test_entity_equals_with_all_same():
    a = EntityDouble(1, 2)
    b = EntityDouble(1, 2)

    assert a == b


def test_entity_equals_with_only_same_id():
    a = EntityDouble(1, 2)
    b = EntityDouble(1, 3)

    assert a == b


def test_entity_not_equal_all_different():
    a = EntityDouble(1, 2)
    b = EntityDouble(2, 3)

    assert a != b


def test_entity_not_equal_with_same_value():
    a = EntityDouble(1, 2)
    b = EntityDouble(2, 2)

    assert a != b


def test_entity_no_hash():
    a = EntityDouble(1, 2)

    try:
        result = hash(a)
        assert False
    except TypeError as e:
        pass


def test_entity_string():
    a = EntityDouble(1, 2)

    assert str(a) == 'EntityDouble(id=1)'


def test_id_id():
    a = IdDouble(1)

    assert a.id == 1


def test_id_table_name():
    a = IdDouble(1)

    assert a.table_name == 'TABLE'


def test_id_string():
    a = IdDouble(1)

    assert str(a) == 'TABLE ID 1'
