import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_addnew(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        # create add contact
        wd = self.app.wd
        self.open_addnew()
        self.contact_form(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return to contact page
        wd.find_element_by_link_text("home").click()

    def contact_form(self, contact):
        wd = self.app.wd
        # self.type_cont(contact)
        self.type_cont("firstname", contact.firstname)
        self.type_cont("lastname", contact.lastname)
        self.type_cont("address", contact.address)
        self.type_cont("mobile", contact.mobile)
        self.type_cont("email", contact.email)
        self.type_cont("byear", contact.byear)

    def type_cont(self, contact_data, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_data).click()
            wd.find_element_by_name(contact_data).clear()
            wd.find_element_by_name(contact_data).send_keys(text)

    def edit_contact(self, contact):
        # edit contact
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # wd.find_element_by_xpath('//img[@src="icons/pencil.png"]').click()
        self.contact_form(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()

    def del_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        # time.sleep(3)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
