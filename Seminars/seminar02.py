# 3.1 Вводим с клавиатуры десятичное число. Необходимо перевести его в двоичную систему счисления.

# def transfer(number, radix):
#     f = ''
#     if radix > 0:
#         if number > 0:
#             while number > 0:
#                 temporary = number % radix
#                 number = number // radix
#                 f = f + str(temporary)
#             number1 = int(f[::-1])
#             print(f"{radix}-ичное представление заданного числа: {number1}")
#         elif number < 0:
#             print('Очень сложное и не факт, что получится')
#
#         else:
#             print("Перевод нуля в любую систему счисления даст ноль.")
#     else:
#         print("Давайте считать, что основанием системы счисления может быть только натуральное число.")
#
#
# num = int(input('Введите число в десятичной системе: '))
# num1 = 2
#
# transfer(num, num1)

# 3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.

# def count_letter(text):
#     count_vowels = 0
#     count_consonants = 0
#     text = text.lower()
#     text = text.replace('.', '')
#     text = text.replace(',', '')
#     text = text.replace(' ', '')
#     text = text.replace('!', '')
#     text = text.replace('?', '')
#     text = text.replace(':', '')
#     text = text.replace(';', '')
#     text = text.replace("'", '')
#     text = text.replace('"', '')
#     text = text.replace('=', '')
#     text = text.replace('/', '')
#     list_of_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#     list_of_letters = ['ъ', 'ь']
#     for i in text:
#         if i in list_of_vowels:
#             count_vowels += 1
#         elif i in list_of_letters:
#             continue
#         else:
#             count_consonants += 1
#     print(f'Гласных букв - {count_vowels}. Согласных - {count_consonants}')
#
#
user_text = input('Введите текст: ')


#
# count_letter(user_text)

# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом

# def palindrome(text):
#     check = False
#     for i in range((len(text) - 1 // 2)):
#         if text[i] is text[(len(text) - 1) - i]:
#             check = True
#         else:
#             check = False
#     if check is True:
#         print('Это палиндром')
#     else:
#         print('Это не палиндром')
#
#
# palindrome(user_text)

# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами


# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре


# 3.6 Безопасный пароль. Пользователь вбивает пароль. Нужно сказать -
# безопасный он или нет. Безопасным считается, если он от 8 символов,
# есть верхний и нижний регистр. А так же цифры. Можеет, при желании, добавить и спец. символы


# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего


# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
