import sqlite3


# 1 Создание базы данных
def create_base():
    name1 = 'sql_base.db'
    try:
        sql_connect = sqlite3.connect(name1)  # Создание файла базы банных sql_base.db
        print("База данных \'sql_base.db\' создана и успешно подключена к SQLite.")
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite.", error)
    finally:
        if (sql_connect):
            sql_connect.close()
            print("Соединение с SQLite закрыто.")
    return name1


# 2 Создание новой таблицы.
# Данные для таблицы:
# CREATE TABLE IF NOT EXISTS telephone_book(id INTEGER PRIMARY KEY, Имя TEXT NOT NULL, Фамилия TEXT NOT NULL, Отчество TEXT NOT NULL,
# Сотовый REAL NOT NULL, Домашний REAL NOT NULL);
def create_new_table():
    try:
        sql_connect = sqlite3.connect('sql_base.db')
        cursor = sql_connect.cursor()  # Создается объект cursor позволяющий делать SQL-запросы к базе.
        telephone_book = '''CREATE TABLE IF NOT EXISTS telephone_book (
                         id INTEGER PRIMARY KEY, Имя TEXT NOT NULL,
                         Фамилия TEXT NOT NULL,
                         Отчество TEXT NOT NULL,
                         Сотовый INTEGER NOT NULL,
                         Домашний INTEGER NOT NULL);'''
        cursor.execute(telephone_book)
        sql_connect.commit()
        print("Таблица \'telephone_book\' создана.")
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite.", error)
    finally:
        if (sql_connect):
            sql_connect.close()
            print("Соединение с SQLite закрыто.")


# 3 Добавление данных в таблицу
def past_dates():
    new_pers = create_new_person()
    try:
        sql_connect = sqlite3.connect('sql_base.db')
        cursor = sql_connect.cursor()
        print("Подключение к SQLite установлено.")
        sql_insert_datas = """INSERT INTO telephone_book
                          (id, Имя, Фамилия, Отчество, Сотовый, Домашний)
                          VALUES
                          (?,?,?,?,?,?);"""
        data_tuple = (new_pers['Id'],
                      new_pers['Имя'],
                      new_pers['Фамилия'],
                      new_pers['Отчество'],
                      new_pers['Сотовый телефон'],
                      new_pers['Домашний телефон'])
        cursor.execute(sql_insert_datas, data_tuple)
        sql_connect.commit()
        print("Запись успешно добавлена в таблицу.", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite.", error)
    finally:
        if (sql_connect):
            sql_connect.close()
            print("Соединение с SQLite закрыто.")


def create_new_person():
    dict1 = {'Id': 0, 'Имя': '', 'Фамилия': '', 'Отчество': '', 'Сотовый телефон': 0, 'Домашний телефон': 0, }
    for (k, v) in dict1.items():
        dict1[k] = input(f"{k} человека: ")
    print(dict1)
    return dict1


def read_all_table(name='sql_base.db'):
    try:
        sqlite_connection = sqlite3.connect(name)
        cursor = sqlite_connection.cursor()
        print("Подключение к SQLite установлено.")
        sql_select_query = """SELECT * from telephone_book"""
        cursor.execute(sql_select_query)
        rec = cursor.fetchall()
        print("Всего строк: ", len(rec))
        print("Вывод каждой строки: ")
        for row in rec:
            print("ID: ", row[0])
            print("Имя: ", row[1])
            print("Фамилия: ", row[2])
            print("Отчество: ", row[3])
            print("Сотовый телефон: ", row[4])
            print("Домашний телефон: ", row[5], end="\n\n")
            print("\n")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def read_single_row(name, key):
    try:
        sqlite_connection = sqlite3.connect('sql_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключение к SQLite установлено.")
        sqlite_select_query = f"""SELECT * from telephone_book where {name} = ?"""
        cursor.execute(sqlite_select_query, (key,))
        print("Чтение одной строки: \n")
        rec = cursor.fetchone()
        print("ID: ", rec[0])
        print("Имя: ", rec[1])
        print("Фамилия: ", rec[2])
        print("Отчество: ", rec[3])
        print("Сотовый телефон: ", rec[4])
        print("Домашний телефон: ", rec[5], end="\n\n")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def update_row_table():
    list1 = list()
    list1.append(create_list('Введите название столбца в котором необходимо найти нужную строку: '))  # List[2]
    list1.append(create_list('Введите значение по которому необходимо определить строку: '))  # List[3]
    list1.append(create_list('Введите название столбца в котором необходимо будет изменить значение, для данной строки: '))  # List[0]
    list1.append(create_list('Введите новое значение: '))  # List[1]
    try:
        sqlite_connection = sqlite3.connect('sql_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключение к SQLite установлено.")
        sql_update_query = f"""Update telephone_book set {list1[2]} = ? where {list1[0]} = ?"""
        data = (list1[3], list1[1])
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена.")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def create_list(name):
    val = input(f"{name}: ")
    return val


def delete_row():
    name1 = create_list('Введине название столбца в котором находится удаляемое значение: ')
    key1 = create_list('Введине значение, находящееся в удаляемой строке, данного столбца: ')
    try:
        sqlite_connection = sqlite3.connect('sql_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключение к SQLite установлено.")

        sql_delete_query = f"""DELETE from telephone_book where {name1} = ?"""
        cursor.execute(sql_delete_query, (key1))
        sqlite_connection.commit()
        print("Запись успешно удалена.")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")
