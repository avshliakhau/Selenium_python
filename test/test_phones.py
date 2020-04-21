import re
from random import randrange


def test_phones_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))  # добавили случайности
    print(index)
    contact_from_home_page = app.contact.get_contact_list()[index] # Страница домашняя с таблицей (тут факса нет)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index) # Edit Страница редактирования
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() /-]", "", s) # !!!то что надо вырезать обязательно в квадр скобках, иначе падает!!!

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone]))))
