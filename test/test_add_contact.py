# -*- coding: utf-8 -*-
from model.contact import Contact


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname = "Iliy", lastname = "Charm", address = "Praha, 8-str. 2C", mobile = "+380351111191", email = "ser35@skoda.cz", byear = "1992")
    app.contact.create_contact(contact)
    # assert len(old_contacts) + 1 == len(new_contacts)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list() # перенесли ниже сравнения длины
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # firstname = "Vlad", lastname = "Pytin", address = "Praha, 99-str. 2C",
    #         home = "11-11-555", mobile = "333-555-77", work = "557-799",

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# def random_string_mix(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# def random_string_dig(prefix, maxlen):
#     symbols = string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [
#     Contact(firstname=random_string("F_", 8), lastname=random_string("L_", 10),
#             address=random_string_mix("P_", 10), home=random_string_dig("+", 10), mobile=random_string_dig("+", 10),
#             email=(random_string_mix("e", 7) + "@" + random_string_mix("a", 7)+ "." + random_string_mix("b", 4)))
#     for i in range(2)
#     ]

