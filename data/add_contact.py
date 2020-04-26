from model.contact import Contact


constant = [
    Contact(firstname="First_1", lastname="Last_1", address="Dom_1", home="tel_home1", mobile="tel_mob1", email="email@bk.ru", email2="1email@bk.ru"),
    Contact(firstname="First_2", lastname="Last_2", address="Dom_2", home="tel_home2", mobile="tel_mob2", email="email@bk.ru", email2="2email@bk.ru")
]

# def random_string(prefix, maxlen): #переносим в generator.contact.py
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
