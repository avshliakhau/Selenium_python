from model.contact import Contact
import time

def test_edit_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Edit+++")
    contact.id = old_contacts[0].id
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    contact = Contact(firstname="Edit+++", lastname="Edit++", mobile="Edit+", byear="1999")
    app.contact.edit_contact(contact)
    # assert len(old_contacts) == len(new_contacts)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list() # перенесли ниже сравнения длины
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    # time.sleep(5)
    # app.session.logout()

# def test_edit_contacttoo(app):
#     # app.session.login(username="admin", password="secret")
#     app.contact.edit_contact(Contact(firstname="777Edit", byear="2020"))
#     # time.sleep(5)
#     # app.session.logout()