# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

from random import randint


def create_array_and_calculate_arithmetic_mean():
    a = int(input('Введите количество строк: '))
    b = int(input('Введите количество столбцов: '))
    if a > 0 and b > 0:
        print()
        print('Произвольный двумерный массив:')
        arithmetic_mean = []
        new_array = []
        for i in range(a):
            new_array.append([[]])
            for j in range(b-1):
                new_array[i].append([])
        for i in range(a):
            arithmetic_mean.append(0)
            for j in range(b):
                new_array[i][j] = randint(1, 100)
                arithmetic_mean[i] += new_array[i][j]
            print(new_array[i])
            arithmetic_mean[i] = round(arithmetic_mean[i]/a, 2)
        print()
        for i in range(len(arithmetic_mean)):
            print(
                f'Среднее арифметическое {i+1}й строки: {arithmetic_mean[i]}')
    else:
        print('Одно или оба введённых числа несоответствуют понятию "количество".')

create_array_and_calculate_arithmetic_mean()

# прошу дать обратную связь по этой задаче, поскольку уверена, что это двумерный массив задаётся как-то иначе