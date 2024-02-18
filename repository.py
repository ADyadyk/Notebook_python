import csv
import datetime

# вывод списка словарей в консоль
def print_dic_to_console(dic_list):
    for dic in dic_list:
        print(dic)

# добавить заметку в виртуальную записную книжку
def add_item(dic_list):
    # найдём наибольший id
    index = 1
    for i in range(len(dic_list)):
        if index < int(dic_list[i]["id"]):
            index = int(dic_list[i]["id"])

    # получим id для следующей записи:
    id_index = index + 1
    # получим заголовок и тело заметки у пользователя
    note_title = input("Введите заголовок заметки: ")
    note_body = input("Введите тело заметки: ")
    # получим дату создания заметки
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    # создадим словарь для заметки
    dic_temp = {'id':str(id_index), 'Заголовок заметки':note_title, 'Тело заметки':note_body, 'Дата':current_date}
    # добавим данный словарь в наш список словарей
    dic_list.append(dic_temp)

# редактировать заметку в виртуальной записной книжке, выбрав её по id
def update_item(dic_list):
    update_item_id = int(input("Введите id заметки, которую необходимо откорректировать: "))
    # поиск в списке словаря по id и удаление его
    update_dic ={}
    for i in range(len(dic_list)):
        if update_item_id == int(dic_list[i]["id"]):
            update_dic = dic_list[i]
    dic_list.remove(update_dic)
    # редактирование заметки
    print('Выберите что вы хотите отредактировать:',
          '1. Заголовок заметки',
          '2. Тело заметки', sep = '\n')
    choice = int(input())
    if choice == 1:
        update_dic['Заголовок заметки'] = input("Введите новый заголовок для заметки: ")
    if choice == 2:
        update_dic['Тело заметки'] = input("Введите новое тело заметки: ")
    # изменение даты заметки
    update_dic['Дата'] = datetime.datetime.now().strftime('%Y-%m-%d')
    # добавление в список изменённой заметки
    dic_list.append(update_dic)

# удалить заметку в виртуальной записной книжке, найдя её по id
def delete_item(dic_list):
    delete_item_id = int(input("Введите id заметки, которую необходимо удалить: "))
    # поиск в списке словаря по id и удаление его
    delete_dic = {}
    for i in range(len(dic_list)):
        if delete_item_id == int(dic_list[i]["id"]):
            delete_dic = dic_list[i]
    dic_list.remove(delete_dic)

# вывести в консоль заметки с одной датой
def choice_item_by_date(dic_list):
    choice_date = input("Введите дату в формате YYYY-MM-DD (например 2020-01-01): ")
    date_dic_list = []
    for i in range(len(dic_list)):
        if choice_date == dic_list[i]["Дата"]:
            date_dic_list.append(dic_list[i])
    print_dic_to_console(date_dic_list)

# вывести в консоль заметку по id
def choice_item_by_id(dic_list):
    update_item_id = int(input("Введите id заметки, которую вы хотите вывести в консоль: "))
    choice_dic = {}
    for i in range(len(dic_list)):
        if update_item_id == int(dic_list[i]["id"]):
            choice_dic = dic_list[i]
    print(choice_dic)

# сохранить все изменения в виртуальной записной книжке в файл
def save_all_changes_to_file(dic_list, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(dic_list[0].keys()), delimiter=';')
        writer.writeheader()
        for d in dic_list:
            writer.writerow(d)