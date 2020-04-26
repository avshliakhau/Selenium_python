from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.implicitly_wait(1)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
            self.wd.implicitly_wait(1)
        elif browser == "ie":
            self.wd = webdriver.Ie()
            self.wd.implicitly_wait(3)
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == (self.base_url) and len(wd.find_elements_by_xpath("//input[@type='button']")) > 1):
            wd.get(self.base_url)
            # wd.get("http://localhost/addressbook/")
        # if not (wd.current_url.startswith("http://localhost/addressbook/") and len(wd.find_elements_by_xpath("//input[@type='button']")) > 1):
        #     wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()

