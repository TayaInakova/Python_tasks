# Допустим, всё, что вводит пользователь - валидно.

#  Задача 1

week = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница', 'суббота', 'воскресенье']
day_of_the_week = int(input('Введите порядковый номер дня недели: '))
if day_of_the_week < 1 or day_of_the_week > 7:
    print('Не существует дня недели с таким номером')
elif day_of_the_week > 0 and day_of_the_week < 6:
    print(f'{week[day_of_the_week - 1]} - будний день.')
else:
    print(f'{week[day_of_the_week - 1]} - выходной день.')
