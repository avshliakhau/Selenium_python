from model.group import Group


def test_edit_group1(app):
    # app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="NewGroupEdit"))
    # app.session.logout()

def test_edit_group2(app):
    # app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(header="NewHeaderEdit", footer="NewFooterEdit"))
    # app.session.logout()