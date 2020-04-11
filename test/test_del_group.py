# -*- coding: utf-8 -*--
from model.group import Group
import time


def test_delete_first_group(app):
    # app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
        # time.sleep(5)
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups) #после того, как добавили проверку по смыслу, эты строку можно и убрать но мы оставим чтобы ошибка (вдруг что) была более понятна
    old_groups[0:1] = [] # удаляем первую строку
    assert old_groups == new_groups# сравниваем старую группу без первой строки и
    # app.session.logout()
