# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором

from random import randint


def create_sort_and_print_random_array(n):
    new_random_array = []
    for i in range(n):
        new_random_array.append(randint(1, 100))
    print(f'Произвольный массив из {n} элементов:')
    print(new_random_array)
    print()
    for i in range(len(new_random_array) - 1):
        for j in range(i+1, len(new_random_array)):
            if new_random_array[j] < new_random_array[i]:
                new_random_array[j], new_random_array[i] = new_random_array[i], new_random_array[j]
    print(f'Отсортированный массив из {n} элементов:')
    print(new_random_array)


create_sort_and_print_random_array(30)
