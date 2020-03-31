# -*- coding: utf-8 -*--
import pytest
from fixture.application import Application
from model.group import Group
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group_1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group #1", header="Header #1", footer="Footer #1"))
    app.session.logout()

def test_add_group_2(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group #2", header="Header #2", footer="Footer #2"))
    app.session.logout()

def test_add_group_3(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group #3", header="Header #3", footer="Footer #3"))
    app.session.logout()

# def test_add_contact1(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.create_contact(Contact(firstname="Kol", lastname="Pol", address="Minsk, Jukova str. 4", mobile="+375296507090", email="serge35@inbox.ru", byear="1995"))
#     app.session.logout()
#
# def test_add_contact2(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.create_contact(Contact(firstname="Maks", lastname="Second", address="Brest, Moskowskay str. 55", mobile="+375336007000", email="ser35@bk.ru", byear="1990"))
#     app.session.logout()
#
# def test_add_contact3(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.create_contact(Contact(firstname="Ilon", lastname="Mask", address="Frisko, 158-str. 12B", mobile="+380356008899", email="ser35@tesla.us", byear="1981"))
#     app.session.logout()
#