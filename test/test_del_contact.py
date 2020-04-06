from model.contact import Contact


def test_del_contact(app):
    # app.session.login(username="admin", password="secret")
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    app.contact.del_first_contact()
    # app.session.logout()