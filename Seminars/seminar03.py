# 1) Есть список: s = ['a', 'b', 'c', 'd', 'e']
# Необходимо написать программу, которая сдвинет список spisok следующим образом: ['c', 'd', 'e', 'a', 'b']

#   срезами

# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#   через цикл и аппенд

# 3) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 4];
# - [2, 3, 5, 6] => [12, 15]

#   перемножаем, i++, последний элемент удаляем. Стоп, когда пройдет половина списка или половина +1(для нечётного количества)

# 4) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#   через циклы и накидывать элементы за один проход на обе стороны списка