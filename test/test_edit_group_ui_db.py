from model.group import Group
import random


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_edit"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)