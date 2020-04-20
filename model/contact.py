# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    # def __init__(self, id=None, firstname=None, lastname=None, address=None,
    # homephone=None, mobilephone=None, workphone=None, fax=None,
    # email=None, email2=None, email3=None, all_phones_from_home_page=None):

    def __init__(self, id=None, firstname=None, lastname=None, homephone=None,
                 mobilephone=None, workphone=None, fax=None, all_phones_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        # self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        # self.email = email
        # self.email2 = email2
        # self.email3 = email3


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.mobilephone)

    def __eq__(self, other):
        return self.lastname == other.lastname and self.firstname == other.firstname and self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):# делаем методом в классе Контакт / параметр (из "ct")превращаем в стандартный self
        if self.id:
            return int(self.id)
        else:
            return maxsize
