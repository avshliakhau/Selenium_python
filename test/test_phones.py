import re
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0] # Страница домашняя с таблицей
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0) # Edit Страница редактирования
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.fax == merge_fax_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    # assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    # assert contact_from_home_page.fax == contact_from_edit_page.faxphone

def test_phones_on_contact_view_page(app):# Страница редактирования контакта
    contact_from_view_page = app.contact.get_contact_from_view_page(0) # Details
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0) # Edit
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.fax == contact_from_edit_page.fax

def clear(s):
    return re.sub("[()/-]", "", s) # !!!то что надо вырезать обязательно в квадр скобках, иначе падает!!!

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone]))))
