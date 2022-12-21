def delete_data_in_planner(data):
    a = input('Выберите день недели, в котором хотите удалить запись:\n Понедельник - 1\n Вторник - 2\n '
              'Среда - 3\n Четверг - 4\n Пятница - 5\n Суббота - 6\n Воскресенье - 7\n')
    try:
        a = int(a)
    except Exception:
        print('Ни один день не выбран.')
        print()
    day_choice = ['Понедельник:\n', 'Вторник:\n', 'Среда:\n', 'Четверг:\n', 'Пятница:\n', 'Суббота:\n',
                  'Воскресенье:\n']
    if a <= len(day_choice):
        changed = int(
            input('Введите порядковый номер записи, которую хотите удалить: '))

        data[day_choice[a - 1]].pop(changed - 1)
        data[day_choice[a - 1]].sort()
        print()
        _ = input('Введите любой символ для возвращения в меню: ')
    else:
        print('Выход')
    return data
