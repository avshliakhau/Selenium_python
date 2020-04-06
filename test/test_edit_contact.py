from model.contact import Contact
import time

def test_edit_contact(app):
    # app.session.login(username="admin", password="secret")
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    app.contact.edit_contact(Contact(firstname="Edit", lastname="Edit", mobile="+Edit", byear="1999"))
    # time.sleep(5)
    # app.session.logout()

def test_edit_contacttoo(app):
    # app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="777Edit", byear="2020"))
    # time.sleep(5)
    # app.session.logout()