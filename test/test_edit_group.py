from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="GroupEdit #3", header="HeaderEdit #3", footer="FooterEdit #3"))
    app.session.logout()