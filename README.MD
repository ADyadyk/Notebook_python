**<big>Краткое описание программы NOTEBOOK</big>**
___
1. При создании программы она была разделена на логические слои:
- view - слой, отвечающий за обработку ввода и вывода данных (simple frontend). К данному слою относятся view.py и menu.py
- controller - логический слой, отвечающий за связь view и model
- model - слой отвечающий за обработку данных (simple backend). К данному слою относится repository.py
2. Запуск программы происходит непосредственно из main.py
3. Меню представлено в menu.py. Обращение к меню происходит из метода run() из view.py
4. В view.py представлен метод run(), который непосредственно взаимодействует с пользователем. Запрашиваемая у пользователя информация передается в слой controller (controller.py), а из него на обработку в model (reposotory.py). Обработанная информация опять же через слой controller (controller.py) передается в слой view (view.py) и потом выводится в консоль пользователю.
5. В слое model (repository.py) представлены следующие методы:
- **print_dic_to_console(dic_list)** - выводит список словарей в консоль
- **add_item(dic_list)** - добавляет заметку в виртуальную записную книжку
- **update_item(dic_list)** - редактирует заметку в виртуальной записной книжке, выбрав её по id
- **delete_item(dic_list)** - удаляет заметку в виртуальной записной книжке, найдя её по id
- **choice_item_by_date(dic_list)** - выводит в консоль заметки с одной датой
- **choice_item_by_id(dic_list)** - выводит в консоль заметку по id
- **save_all_changes_to_file(dic_list, filename)** - сохранить все изменения в виртуальной записной книжке в файл