import open_planner
import view_data
import add_data
import change_data
import delete_data


def choosing_action():
    print('Меню:\n')
    q = input(
        ' Показать расписание - 0\n Новая запись - 1\n Изменить запись - 2\n Удалить запись - 3\n')
    try:
        q = int(q)
    except Exception:
        print('Ни один пункт меню не выбран.')
    print()

    return q


def main_menu_start():
    new_planner = open_planner.read_daily_planner_file()
    a = input('Для доступа в меню введите "*"\n')
    while a == '*':
        choice = choosing_action()
        if choice == 0:
            view_data.planner_view(new_planner)
            print()
        elif choice == 1:
            open_planner.rewrite_planner(add_data.add_new_data(new_planner))
            print()
        elif choice == 2:
            open_planner.rewrite_planner(change_data.change_data_in_planner(new_planner))
            print()
        elif choice == 3:
            open_planner.rewrite_planner(delete_data.delete_data_in_planner(new_planner))
            print()
        else:
            a = 0
    else:
        print('Работа с расписанием завершена')
