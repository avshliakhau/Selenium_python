# -*- coding: utf-8 -*--
from selenium import webdriver
from group import Group
import unittest, time

class tast_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        # login-user
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("groups").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_add_group1(self):
        wd = self.wd
        # self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        # self.open_groups_page(wd)
        self.create_group(wd, Group(name="Group #1", header="Header #1", footer="Footer #1"))
        # self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_group2(self):
        wd = self.wd
        # self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        # self.open_groups_page(wd)
        self.create_group(wd, Group(name="Group #2", header="Header #2", footer="Footer #2"))
        # self.return_to_groups_page(wd)
        self.logout(wd)

    # time.sleep(10)
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()