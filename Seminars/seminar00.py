# Семинар 1


# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# if a == b**0.5 or b == a**0.5:
#     print('Одно число являеся квадратом другого')
# else:
#     print('Ни одно из чисел являеся квадратом другого')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# a01 = int(input('Введите число: '))
# a02 = int(input('Введите число: '))
# a03 = int(input('Введите число: '))
# a04 = int(input('Введите число: '))
# a05 = int(input('Введите число: '))
# the_maximum_of_the_numbers = a01
# if a02 > the_maximum_of_the_numbers:
#     the_maximum_of_the_numbers = a02
# if a03 > the_maximum_of_the_numbers:
#     the_maximum_of_the_numbers = a03
# if a04 > the_maximum_of_the_numbers:
#     the_maximum_of_the_numbers = a04
# if a05 > the_maximum_of_the_numbers:
#     the_maximum_of_the_numbers = a05
# print(the_maximum_of_the_numbers)


# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# num = int(input('Введите число: '))
# if num > 0:
#     z = -1
#     sequence = num * 2 + 1
# elif num < 0:
#     z = 1
#     sequence = (-num * 2) + 1
# for i in range(sequence):
#     print(num)
#     num += z


# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# fraction = float(input('Введите число: '))
# if number_of_rounds(fraction) == fraction:
#     print('У числа нет дробной части')
# else:
#     the_first_digit = (int(fraction * 10)) % 10
#     print(the_first_digit)


# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# digit = int(input('Введите число: '))
# if (digit % 5 == 0 and digit % 10 == 0) or (digit % 15 == 0 and digit % 30 != 0):
#     print(True)
# else:
#     print(False)

