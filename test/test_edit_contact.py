from model.contact import Contact
from random import randrange
import time


def test_edit_some_contact(app):

    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))

    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname="Edit")
    index = randrange(len(old_contacts)) # добавили случайности
    contact = Contact(firstname="EditEdit", lastname="Edit_Edit", mobile="Edit_", byear="2005")
    contact.id = old_contacts[index].id # идентификатор тоже запоминаем
    # contact = Contact(firstname="EditEdit", lastname="Edit_Edit", mobile="Edit_", byear="2005")
    # index = randrange(len(old_contacts))  # добавили случайности
    app.contact.edit_contact_by_index(index, contact)
    # assert len(old_contacts) == len(new_contacts)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list() # перенесли ниже сравнения длины
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Edit+++")
#     contact.id = old_contacts[0].id
#     if app.contact.count_contact() == 0:
#         app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
#     contact = Contact(firstname="Edit+++", lastname="Edit++", mobile="Edit+", byear="1999")
#     app.contact.edit_contact(contact)
#     # assert len(old_contacts) == len(new_contacts)
#     assert len(old_contacts) == app.contact.count_contact()
#     new_contacts = app.contact.get_contact_list() # перенесли ниже сравнения длины
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)