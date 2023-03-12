from functions import *


def launch_phone_book():
    bd_name = create_base()  # Создание базы данных - sql_base.db
    create_new_table()  # Создание таблицы в базе данных - telephone_book

    while True:
        command = input("Введите комманду: ")

        if command == 'add':  # Добавление данных в справочник
            past_dates()
        elif command == 'show_all':  # Показать весь справочник
            read_all_table()
        elif command == 'show':  # Поиск строки в справочнике по значению в указанном столбце
            name_word = input("Введите имя столбца: ")
            key_word = input("Введите название для поиска: ")
            read_single_row(name_word, key_word)
        elif command == 'help':  # Просмотр справки
            print("Список доступных команд:\n\t"
                  "add - Добавить данные в справочник\n\t"
                  "edit - Редактировать запись\n\t"
                  "show_all - Показать весь справочник\n\t"
                  "show- Поиск строки в справочнике по значению в указанном столбце\n\t"
                  "help - Просмотр справки\n\t"
                  "stop - Завершить работу справочника\n\t"
                  "del_one - Удалить запись из справочника\n\t")
        elif command == 'edit':  # Редактировать запись в справочнике
            update_row_table()
        elif command == 'del_one':  # Удалить строку в справочнике
            delete_row()
        elif command == 'stop':  # Завершить работу справочника
            print("Работа справочника завершена.")
            exit()
        else:
            print("Неизвестная команда. Обратитесь к справке, введите help.")


launch_phone_book()
