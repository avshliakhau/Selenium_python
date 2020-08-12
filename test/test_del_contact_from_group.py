from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_group_create", header="test_header_create", footer="test_footer_create"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.del_contact_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)
