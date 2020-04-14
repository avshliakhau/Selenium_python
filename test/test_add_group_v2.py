# -*- coding: utf-8 -*--

from model.group import Group


def test_add_group_1(app):
    # app.session.login(username="admin", password="secret") # убираем лишнюю строку
    old_groups = app.group.get_group_list()
    group = Group(name="Group #11", header="Header #11", footer="Footer #11")
    app.group.create(group)
    # assert len(old_groups) + 1 == len(new_groups)
    assert len(old_groups) + 1 == app.group.count()# вначале сравниваем длины списка старого +1 и длину count и только при совпадении сравниваем сами списки
    new_groups = app.group.get_group_list() # перенесли ниже сравнения длины
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # в качестве ключа будет использоваться метод Group
    # app.session.logout() # убираем лишнюю строку

# def test_add_group_2(app):
#     # app.session.login(username="admin", password="secret") # убираем лишнюю строку
#     old_groups = app.group.get_group_list()
#     group = Group(name="Group #22", header="Header #22", footer="Footer #22")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#     # app.session.logout() # убираем лишнюю строку
# #
# def test_add_group_3(app):
#     # app.session.login(username="admin", password="secret") # убираем лишнюю строку
#     old_groups = app.group.get_group_list()
#     group = Group(name="Group #33")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#     # app.session.logout() # убираем лишнюю строку
