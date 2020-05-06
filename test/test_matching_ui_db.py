from model.contact import Contact


def test_matching_ui_db(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = db.get_contact_list()
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    # print("web", sorted(ui_list, key=Contact.id_or_max))
    # print("dat", sorted(db_list, key=Contact.id_or_max))
