from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app):
    old_contacts = db.get_contact_list() #
    contact = random.choice(old_contacts)
    if len(db.get_contacts_in_group(Group(id="811"))) == 0:
        app.contact.add_contact_to_group_by_id(contact.id)
        print(len(db.get_contacts_in_group(Group(id="811"))))
    old_contacts_in_group = db.get_contacts_in_group(Group(id="811"))#
    contact = random.choice(old_contacts_in_group)
    print(contact)
    app.contact.del_contact_from_group_by_id(contact.id)
    new_contacts = db.get_contacts_in_group(Group(id="811"))
    new_contacts_not = db.get_contacts_not_in_group(Group(id="811"))
    # print(new_contacts)
    # print(new_contacts_not)
    # print(len(new_contacts))
    assert len(old_contacts_in_group) - 1 == len(new_contacts)
    if len(old_contacts) == len(db.get_contacts_in_group(Group(id="811"))) + len(db.get_contacts_not_in_group(Group(id="811"))):
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted((new_contacts + new_contacts_not), key=Contact.id_or_max)