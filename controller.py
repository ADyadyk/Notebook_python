import repository as rep

def print_dic_to_console_controller(dic_list):
    rep.print_dic_to_console(dic_list)

def add_item_controller(dic_list):
    rep.add_item(dic_list)

def update_item_controller(dic_list):
    rep.update_item(dic_list)

def delete_item_controller(dic_list):
    rep.delete_item(dic_list)

def choice_item_by_date_controller(dic_list):
    rep.choice_item_by_date(dic_list)

def choice_item_by_id_controller(dic_list):
    rep.choice_item_by_id(dic_list)

def save_all_changes_to_file_controller(dic_list, filename):
    rep.save_all_changes_to_file(dic_list, filename)