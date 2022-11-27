# Допустим, всё, что вводит пользователь - валидно.

# Задача 2

quantity = int(input('Введите количество чисел: '))
first_max = None
second_max = None
if quantity > 0:
    for i in range(quantity):
        i = int(input('Введите число: '))
        if first_max is None:
            first_max = i
        elif i > first_max:
            second_max = first_max
            first_max = i
        elif i < first_max and second_max is None or second_max is not None and second_max < i < first_max:
            second_max = i
    if first_max is not None:
        print(f'Максимальное из перечисленных чисел: {first_max}.')
    if second_max is not None:
        print(f'Второе максимальное из перечисленных чисел: {second_max}.')
else:
    print('Нет чисел для сравнения')
