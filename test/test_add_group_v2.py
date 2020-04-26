# -*- coding: utf-8 -*--
from model.group import Group
from data.add_group import testdata
# from data.add_group import constant as testdata
import pytest



@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()# вначале сравниваем длины списка старого +1 и длину count и только при совпадении сравниваем сами списки
    new_groups = app.group.get_group_list() # перенесли ниже сравнения длины
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # в качестве ключа будет использоваться метод из класса Group

# def random_string(prefix, maxlen): #///выносим в файл add_group.py & add_data.py
#     symbols = string.ascii_letters + string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [
#     Group(name=random_string("Group", 10), header=random_string("Head", 15), footer=random_string("Foot", 12))
#     for i in range(4)
#     ]

## testdata = [ #///выносим в файл add_group.py & add_data.py
##     Group(name=name, header=header, footer=footer)
##     for name in ["", random_string("name", 10)]
##     for header in ["", random_string("header", 15)]
##     for footer in ["", random_string("footer", 20)]
##     ]


