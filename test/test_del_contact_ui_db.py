from model.contact import Contact
import random

def test_del_some_contact(app, db, check_ui):
    # app.session.login(username="admin", password="secret")
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    # index = randrange(len(old_contacts)) #добавили случайности
    app.contact.del_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts) # можно убрать, но мы оставим (если вдруг ошибка, то более понятное сообщение)
    # old_contacts[index:index+1] =
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)