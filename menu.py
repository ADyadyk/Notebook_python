# Метод выводящий меню:
def show_menu():
    print('Выберите номер пункта в меню:',
          '1. Вывести данные из файла в консоль',
          '2. Вывести в консоль все записи от одной даты',
          '3. Вывести в консоль запись по id',
          '4. Добавить запись',
          '5. Редактировать запись, найдя её по id',
          '6. Удалить запись по id номеру',
          '7. Сохранить все изменения в файл',
          '8. Сохранить изменения в файл и завершить работу',
          '9. Завершить работу не сохраняя изменения', sep = '\n')
    choice = int(input())
    return choice