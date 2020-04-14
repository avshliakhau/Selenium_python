from model.group import Group
import time


def test_edit_group1(app):
    # app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
        time.sleep(2)
    old_groups = app.group.get_group_list()
    group = Group(name="NewGroupEdit", footer="NewFooterEdit")
    group.id = old_groups[0].id # идентификатор тоже запоминаем
    app.group.edit_group(group)
    # assert len(old_groups) == len(new_groups)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list() # перенесли ниже сравнения длины
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # app.session.logout()




# def test_edit_group2(app):
#     # app.session.login(username="admin", password="secret")
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#         time.sleep(2)
#     old_groups = app.group.get_group_list()
#     app.group.edit_group(Group(name="Edit_NameGroup", header="Group_Edit", footer="Footer_Edit"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     # app.session.logout()