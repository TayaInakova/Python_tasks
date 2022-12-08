# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_element(user_list):
    sum_element_case = 0
    for i in range(len(user_list)):
        if i % 2 != 0:
            sum_element_case += user_list[i]
    print(f'Сумма элементов на нечётных поициях: {sum_element_case}')
    return sum_element_case


user_input_list = [5, 8, 33, 7, 59, 1, 0, 5, 2, 4]

sum_list = sum_element(user_input_list)
