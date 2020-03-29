# -*- coding: utf-8 -*--
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group #1", header="Header #1", footer="Footer #1"))
    app.session.logout()

def test_add_group2(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group #2", header="Header #2", footer="Footer #2"))
    app.session.logout()

def test_add_group3(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group #3", header="Header #3", footer="Footer #3"))
    app.session.logout()