from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == ("http://localhost/addressbook/") and len(wd.find_elements_by_xpath("//input[@type='button']")) > 1):
            wd.get("http://localhost/addressbook/")
        # if not (wd.current_url.startswith("http://localhost/addressbook/") and len(wd.find_elements_by_xpath("//input[@type='button']")) > 1):
        #     wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()

