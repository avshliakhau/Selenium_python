# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.support.ui import Select
import unittest, time


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    # test open home page
    def open_home_page(self, wd):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        # login-user
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, wd):
        # create add contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Kol")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Pol")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Minsk, Jukova str. 4")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+375296507090")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("serge35@inbox.ru")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='19']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='June']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1995")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_contact_page(self, wd):
        # return to contact page
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        # time.sleep(5)
        self.login(wd)
        # time.sleep(5)
        self.create_contact(wd)
        # time.sleep(5)
        self.return_to_contact_page(wd)
        # time.sleep(5)
        self.logout(wd)
        # time.sleep(5)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()