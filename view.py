import csv
import controller as con
import menu as m

def run():

    # прочитаем csv файл в словарь
    with open('data.csv', mode='r') as file:
        # создаём cvs reader
        csv_reader = csv.DictReader(file, delimiter=';')
        # создаём список словарей
        notebook = []
        # проходим по строкам в файле
        for row in csv_reader:
            # добавляем полученные словари из строк в список
            notebook.append(row)

    # выбор пункта меню
    choice = m.show_menu()
    print()
    while (choice != 9):
        # вывести все заметки в консоль
        if choice == 1:
            con.print_dic_to_console_controller(notebook)

        # вывести в консоль все заметки с одной датой
        if choice == 2:
            con.choice_item_by_date_controller(notebook)
            print()

        # вывести в консоль заметку, найденную по id
        if choice == 3:
            con.choice_item_by_id_controller(notebook)
            print()

        # добавить заметку в виртуальную записную книжку
        if choice == 4:
            con.add_item_controller(notebook)
            con.print_dic_to_console_controller(notebook)
            print()

        # редактировать заметку в виртуальной записной книжке, найдя её по id
        if choice == 5:
            con.update_item_controller(notebook)
            print()

        # удалить заметку в виртуальной записной книжке, найдя её по id
        if choice == 6:
            con.delete_item_controller(notebook)
            print()

        # сохранить все изменения в виртуальной записной книжке в файл
        if choice == 7:
            con.save_all_changes_to_file_controller(notebook,'data.csv')
            print()

        # сохранить все изменения в виртуальной записной книжке в файл и завершить работу
        if choice == 8:
            con.save_all_changes_to_file_controller(notebook, 'data.csv')
            return
        choice = m.show_menu()
