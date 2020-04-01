from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="firstnameEdit", lastname="lastnameEdit", address="addressEdit", mobile="+Edit", email="edit@inbox.ru", byear="1990"))
    app.session.logout()