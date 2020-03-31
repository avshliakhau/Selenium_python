# -*- coding: utf-8 -*-
import pytest
from fixture.applic import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact1(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Kol", lastname="Pol", address="Minsk, Jukova str. 4",
                                        mobile="+375296507090", email="serge35@inbox.ru", byear="1995"))
    app.logout()

def test_add_contact2(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Maks", lastname="Second", address="Brest, Moskowskay str. 55",
                                        mobile="+375336007000", email="ser35@bk.ru", byear="1990"))
    app.logout()
