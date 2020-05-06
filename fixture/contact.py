from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_addnew(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("photo")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        # create add contact
        wd = self.app.wd
        self.open_addnew()
        self.contact_form(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return to contact page
        self.open_home_page()
        self.contact_cache = None

    def contact_form(self, contact):
        wd = self.app.wd
        # self.type_cont(contact)
        self.type_cont("firstname", contact.firstname)
        self.type_cont("lastname", contact.lastname)
        self.type_cont("address", contact.address)
        self.type_cont("home", contact.home)
        self.type_cont("mobile", contact.mobile)
        self.type_cont("work", contact.work)
        self.type_cont("email", contact.email)
        # self.type_cont("byear", contact.byear)

    def type_cont(self, contact_data, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_data).click()
            wd.find_element_by_name(contact_data).clear()
            wd.find_element_by_name(contact_data).send_keys(text)

    def edit_contact_by_index(self, index, contact):
        # edit contact
        wd = self.app.wd
        self.app.open_home_page()
        # self.open_home_page()
        # self.select_contact_by_index(index)
        wd.find_elements_by_css_selector('table td:nth-child(8)')[index].click()
        self.contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        # edit contact
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.get('input["http://localhost/addressbook/edit.php?id=%s"]' % id)
        # wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # wd.find_elements_by_css_selector('table td:nth-child(8)')[
        #     index].click()
        # wd.find_element_by_css_selector("input[wd.current_url.endswith('/edit.php?id=%s')]" % id).click()
        self.contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_contact(self):
        self.edit_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        # self.app.open_home_page()
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept() # закрытие диалогового окна // тест проходит, но всегда пишет оговорку
        self.open_home_page()
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        # self.app.open_home_page()
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept() # закрытие диалогового окна // тест проходит, но всегда пишет оговорку
        self.open_home_page()
        self.contact_cache = None

    def del_first_contact(self):
        wd = self.app.wd
        self.del_contact_by_index(0)

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        # wd.find_elements_by_name("selected[]")[id].click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):# Страница домашняя с таблицей
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                last = element.find_element_by_css_selector('table td:nth-child(2)').text
                first = element.find_element_by_css_selector('table td:nth-child(3)').text
                address = element.find_element_by_css_selector('table td:nth-child(4)').text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_css_selector('table td:nth-child(6)').text
                # all_phone = element.find_element_by_css_selector('table td:nth-child(6)').text.splitlines()
                all_email = element.find_element_by_css_selector('table td:nth-child(5)').text
                self.contact_cache.append(Contact(id=id, lastname=last, firstname=first, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page = all_email))
            print(self.contact_cache)
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):# Edit Страница редактирования контакта
        wd = self.app.wd
        # self.edit_contact_by_index(index)
        # self.open_contact_view_by_index(index) # Details
        self.open_view_contact_by_index(index) # Edit
        id = wd.find_element_by_name('id').get_attribute("value")
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        address = wd.find_element_by_name('address').text #get_attribute("cols")
        home = wd.find_element_by_name('home').get_attribute("value")
        mobile = wd.find_element_by_name('mobile').get_attribute("value")
        work = wd.find_element_by_name('work').get_attribute("value")
        fax = wd.find_element_by_name('fax').get_attribute("value")
        email = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       home=home, mobile=mobile, work=work, fax=fax,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):# Details страница с деталями контакта
        wd = self.app.wd
        # self.open_view_contact_by_index(index) # Edit
        self.open_contact_view_by_index(index) # Details
        text = wd.find_element_by_xpath('//*[@id="content"]').text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        email = re.search("/^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$/i (.*@.*)", text)
        # email = re.search("@ (.*@.*)", text)
        email2 = re.search("/^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$/i (.*@.*)", text)
        # email2 = re.search("@ (.*@.*)", text)
        email3 = re.search("/^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$/i (.*@.*)", text)
        # email3 = re.search("@ (.*@.*)", text)
        return Contact(home=home, mobile=mobile, work=work, fax=fax,
                       email=email, email2=email2, email3=email3)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_css_selector('table td:nth-child(7)')[index].click()
        # time.sleep(5)

    def open_view_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_css_selector('table td:nth-child(8)')[index].click()
        # time.sleep(5)

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.open_home_page()
    #         self.contact_cache = []
    #         for row in wd.find_elements_by_name('entry'):
    #             cells = row.find_elements_by_name('td')
    #             last = cells[1].text
    #             first = cells[2].text
    #             id = cells[0].find_element_by_name("selected[]").get_attribute("value")
    #             all_phone = cells[5].text.splitlines()
    #             self.contact_cache.append(Contact(id=id, lastname=last, firstname=first,
    #                                               homephone=all_phone[0], mobilephone=all_phone[1],
    #                                               workphone=all_phone[2]))
    #         print(self.contact_cache)
    #     return list(self.contact_cache)