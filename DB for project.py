import sqlite3

# Зєднання з базою даних
conn = sqlite3.connect('database.db')
# Курсор - обєкт який робить запити і отримує результати запитів
cursor = conn.cursor()


# Функція для додавання жителя в БД
def add_resident(login, password, name, surname, street, appart_num):
    cursor.execute(
        "INSERT INTO Residents VALUES (Null, {}, {}, {}, {}, {}, {})".format(login, password, name, surname, street,
                                                                             appart_num))


# Закриваєм зєднання з базою даних
conn.close()
