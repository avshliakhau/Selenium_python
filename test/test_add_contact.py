# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact1(app):
    # app.session.login(username="admin", password="secret")
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "Iliy", lastname = "Charm", address = "Praha, 8-str. 2C", mobile = "+380351111191", email = "ser35@skoda.cz", byear = "1992")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    # def id_or_max(ct): # функцию для вычисления ключа выносим в model/contact.py
    #     if ct.id:
    #         return int(ct.id)
    #     else:
    #         return maxsize
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # print (new_contacts)

# def test_add_contact2(app):
#     # app.session.login(username="admin", password="secret")
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Nik", lastname="Soap", address="Moskow, Jukova str. 1891", mobile="+375296500000", email="ge44@inbox.ru", byear="1983")
#     app.contact.create_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     # app.session.logout()
#
# def test_add_contact3(app):
#     # app.session.login(username="admin", password="secret")
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname = "Jon", lastname = "Postman", address = "Hamburg, Moskowskay str. 77", mobile = "+375336088888", email = "res@bk.ru", byear = "1969")
#     app.contact.create_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     # app.session.logout()


