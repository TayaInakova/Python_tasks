# Допустим, всё, что вводит пользователь - валидно.

# Задача 4

quarter = int(
    input('Введите четверть координатной плоскости, в которой находится точка А: '))
if quarter < 1 or quarter > 4:
    print('У координатной плоскости 4 четверти. Ваше число вне этого диапазона.')
elif quarter == 1:
    print('Координаты по оси х и оси у: от 0 до +∞')
elif quarter == 2:
    print('Координаты по оси х: от 0 до -∞, по оси у: от 0 до +∞')
elif quarter == 3:
    print('Координаты по оси х и оси у: от 0 до -∞')
elif quarter == 4:
    print('Координаты по оси х: от 0 до +∞, по оси у: от 0 до -∞')
