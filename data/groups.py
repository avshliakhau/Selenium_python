from model.group import Group


testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# def random_string(prefix, maxlen): #переносим в generator.group.py
#     symbols = string.ascii_letters + string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [
#     Group(name=random_string("Group", 10), header=random_string("Head", 15), footer=random_string("Foot", 12))
#     for i in range(3)
#     ]
