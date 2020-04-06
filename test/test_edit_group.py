from model.group import Group
import time


def test_edit_group1(app):
    # app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
        time.sleep(2)
    app.group.edit_group(Group(name="NewGroupEdit", footer="NewFooterEdit"))
    # app.session.logout()

def test_edit_group2(app):
    # app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
        time.sleep(2)
    app.group.edit_group(Group(name="Edit_NameGroup", header="Group_Edit", footer="Footer_Edit"))
    # app.session.logout()