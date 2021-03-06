# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact1(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Kol", lastname="Pol", address="Minsk, Jukova str. 4", mobile="+375296507090", email="serge35@inbox.ru", byear="1995"))
    app.session.logout()

def test_add_contact2(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Maks", lastname="Second", address="Brest, Moskowskay str. 55", mobile="+375336007000", email="ser35@bk.ru", byear="1990"))
    app.session.logout()

def test_add_contact3(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Ilon", lastname="Mask", address="Frisko, 158-str. 12B", mobile="+380356008899", email="ser35@tesla.us", byear="1981"))
    app.session.logout()
#
