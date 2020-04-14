from model.contact import Contact


def test_del_contact(app):
    # app.session.login(username="admin", password="secret")
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="test_create", lastname="Test_Create"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts) # можно убрать, но мы оставим (если вдруг ошибка, то более понятное сообщение)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
