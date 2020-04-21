from model.group import Group
import time
import pytest
from random import randrange
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Group(name=random_string("edit_N", 10), header=random_string("edit_h", 10), footer=random_string("edit_f", 10))
    for i in range(5)
    ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_edit_group(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id # идентификатор тоже запоминаем
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list() # перенесли ниже сравнения длины
    old_groups[index] = group
    # time.sleep(1)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # time.sleep(1)