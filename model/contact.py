# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, mobile=None, email=None, byear=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.email = email
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return self.lastname == other.lastname and self.firstname == other.firstname and self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):# делаем методом в классе Контакт / параметр (из "ct")превращаем в стандартный self
        if self.id:
            return int(self.id)
        else:
            return maxsize
