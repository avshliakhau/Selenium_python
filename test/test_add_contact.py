# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact1(self):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Kol", lastname="Pol", address="Minsk, Jukova str. 4",
                                    mobile="+375296507090", email="serge35@inbox.ru", bday="19", bmonth="June", byear="1995"))
    app.logout()

# def test_add_contact2(self):
#     app.login(username="admin", password="secret")
#     app.create_contact(Contact(firstname="Maks", lastname="Second", address="Brest, Moskowskay str. 55",
#                                         mobile="+375336007000", email="ser35@bk.ru", bday="22", bmonth="July", byear="1990"))
#     app.logout()
#
