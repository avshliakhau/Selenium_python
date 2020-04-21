from random import randrange
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_mix(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_dig(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_string("Ed_F_", 10), lastname=random_string("Ed_L_", 10),
            address=random_string_mix("Ed_A_", 10), home=random_string_dig("+", 10),
            email=(random_string_mix("e", 7) + "@" + random_string_mix("a", 7)+ "." + random_string_mix("b", 4)))
    for i in range(2)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_edit_some_contact(app, contact):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts)) # добавили случайности
    contact.id = old_contacts[index].id # идентификатор тоже запоминаем
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list() # перенесли ниже сравнения длины
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
