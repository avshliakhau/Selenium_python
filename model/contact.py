# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, address=None, home=None,
                 mobile=None, work=None, fax=None, all_phones_from_home_page=None,
                 all_email_from_home_page=None, email=None, email2=None, email3=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.all_email_from_home_page = all_email_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,
                                      self.address, self.home, self.email)

    def __eq__(self, other):
        return self.lastname == other.lastname and self.firstname == other.firstname and self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):# делаем методом в классе Контакт / параметр (из "ct")превращаем в стандартный self
        if self.id:
            return int(self.id)
        else:
            return maxsize
