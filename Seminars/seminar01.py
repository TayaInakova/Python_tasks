# Семинар 2
#
# 1) Решить следующую задачу:
# генерируем среднее арифметическое последовательности дробных чисел, вводимых с клавиатуры.
# После того, как введем последнее число  - программа выводит среднее арифметическое,
# максимальное и минимальное значение. (не пользуемся списками и встроенными функциями)
# Количество чисел задаётся в начале работы программы
#
# count = int(input('Задайте количество чисел: '))
# aggregate = 0
# most_of_all = None
# least_of_all = None
# if count >= 0:
#     for i in range(count):
#         i = float(input('Введите дробное число: '))
#         aggregate += i
#         if most_of_all is None:
#             most_of_all = i
#             least_of_all = i
#         elif i > most_of_all:
#             most_of_all = i
#         elif i < least_of_all:
#             least_of_all = i
#     arithmetic_mean = number_of_rounds(aggregate/count, 2)
#     print(f'Среднее арифметическое введенных чисел: {arithmetic_mean}')
#     print(f'Максимальное из введенных чисел: {most_of_all}')
#     print(f'Минимальное из введенных чисел: {least_of_all}')
# else:
#     print('Нет чисел')
#
#
# 2) Решить следующую задачу:Вывести на экран таблицу умножения на заданное число.
#
# num = int(input('Введите число: '))
# for i in range(1, 11):
#     print(f'{i} * {num} = {i * num}')
#
#
# 3) Решить следующую задачу, проверки знания таблицы умножения.
# Программа выводит 10 примеров и выставляет за 10 правильных ответов - пять, за 9 и 8 - 4 балла, за меньше - три.
# Если пользователь ошибся в каком-то ответе - сообщаем ему об этом
# В итоге выводим количество верных ответов и оценку
#
# correct = 0
# for i in range(1, 11):
#     num = int(input(f'Решите пример(введите число): {i} * 2 = '))
#     if num == i * 4:
#         correct += 1
#     else:
#         print('Вы ошиблись')
# print(f'Правильных ответов: {correct}')
# if correct == 10:
#     print('Оценка 5')
# elif 7 < correct < 10:
#     print('Оценка 4')
# if correct < 8:
#     print('Оценка 3')
#
#
# 4) Решить следующую задачу,, выводящие на экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник

# import time
# hour = int(input('Укажите количество часов: '))
# minute = int(input('Укажите количество минут: '))
# second = int(input('Укажите количество секунд: '))
# time_count = second + (minute * 60) + (hour * 3600)
#
#
# def dec(n, end: list[str]):
#     if n % 10 == 1 and n % 100 != 11:
#         return end[0]
#     elif (n % 10 == 2 or n % 10 == 3 or n % 10 == 4) and (n % 100 != 12 or n % 100 != 13 or n % 100 != 14):
#         return end[1]
#     else:
#         return end[2]
#
#
# end_h = ['час', 'часа', 'часов']
# end_m = ['минута', 'минуты', 'минут']
# end_s = ['секунда', 'секунды', 'секунд']
#
# for i in range(time_count, 0, -1):
#     if hour == 0 and minute == 0:
#         second -= 1
#     elif hour == 0:
#         if second == 0:
#             minute -= 1
#             second = 60
#         second -= 1
#     else:
#         if minute == 0 and second == 0:
#             hour -= 1
#             minute = 60
#         if second == 0:
#             minute -= 1
#             second = 60
#         second -= 1
#     time.sleep(1)
#     print(
#         f'Осталось {hour} {dec(hour, end_h)}, {minute} {dec(minute, end_m)}, {second} {dec(second, end_s)}')
#
# print('БЗЗЗЗЗЗЗЗ!')

# 5) Решить следующую задачу, которая вычисляет наибольший общий делитель двух целых чисел
#
# Большее число поделить на меньшее.
# Меньшее число поделить на остаток, который получается после деления.
# Первый остаток поделить на второй остаток.
# Второй остаток поделить на третий и т. д.
# Деление продолжается до тех пор, пока в остатке не получится нуль.
# Последний делитель и есть наибольший общий делитель.
#
# num01 = int(input('Введите первое число: '))
# num02 = int(input('Введите второе число: '))
# num_num = 0
# if num02 > num01:
#     num02, num01 = num01, num02
# while num01 != 0 or num02 != 0:
#     if num02 != 0:
#         num_num = num02
#         num01 = num01 % num020
#
#     else:
#         break
#     if num01 != 0:
#         num_num = num01
#         num02 = num02 % num01
#     else:
#         break
# print(f'Наибольший общий делитель: {num_num}')
