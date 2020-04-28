from model.contact import Contact
import random
import string
import os.path
import json
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 4
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    Contact(firstname=random_string("F_", 8), lastname=random_string("L_", 10),
            address=random_string_mix("P_", 10), home=random_string_dig("+", 10), mobile=random_string_dig("+", 10),
            email=(random_string_mix("e", 7) + "@" + random_string_mix("a", 7)+ "." + random_string_mix("b", 4)))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2) # работает!!!
    out.write(jsonpickle.encode(testdata)) # работает даже без "set_encoder_options" если добавить indent=2!!!