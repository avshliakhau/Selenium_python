# -*- coding: utf-8 -*--
from selenium import webdriver
import unittest

class tast_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
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

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group #1")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("header #1")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("footer #1")
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("groups").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()