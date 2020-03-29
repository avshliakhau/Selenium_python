# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from model.contact import Contact


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    # test open home page
    def open_home_page(self, wd):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        # login-user
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, wd, contact):
        # create add contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # wd.find_element_by_name("bday").click()
        # wd.find_element_by_xpath("//option[@value='19']").click()
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        # wd.find_element_by_name("bmonth").click()
        # wd.find_element_by_xpath("//option[@value='June']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_contact_page(self, wd):
        # return to contact page
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact1(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Kol", lastname="Pol", address="Minsk, Jukova str. 4", mobile="+375296507090", email="serge35@inbox.ru", bday="19", bmonth="June", byear="1995"))
        self.return_to_contact_page(wd)
        self.logout(wd)

    def test_add_contact2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Maks", lastname="Second", address="Brest, Moskowskay str. 55",
                                        mobile="+375336007000", email="ser35@bk.ru", bday="22", bmonth="July", byear="1990"))
        self.return_to_contact_page(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()