from model.contact import Contact
import re


def test_data_ui_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    old_contacts = app.contact.get_contact_list()
    index = len(old_contacts)  # количество контактов в списке
    print(index)
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max) #отсортированная/ главная страница с таблицей
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)  # отсортированная DB (база данных)
    for element in range(index):
        # assert contact_from_home_page[element] == contact_from_db[element]#c cортированными списками = получается! и цикл проходит по всем элементам
        assert contact_from_home_page[element].id == contact_from_db[element].id
        assert contact_from_home_page[element].firstname == contact_from_db[element].firstname
        assert contact_from_home_page[element].lastname == contact_from_db[element].lastname
        assert contact_from_home_page[element].address == contact_from_db[element].address
        assert contact_from_home_page[element].all_phones_from_home_page == merge_phones_like(contact_from_db[element])
        assert contact_from_home_page[element].all_email_from_home_page == merge_email_like(contact_from_db[element])
        # print(contact_from_home_page[element].all_phones_from_home_page)
        # print(contact_from_db[element])

def clear(s):
    return re.sub("[() /-]", "", s) # !!!то что надо вырезать обязательно в квадр скобках, иначе падает!!!

def merge_email_like(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))

def merge_phones_like(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.home, contact.mobile, contact.work]))))