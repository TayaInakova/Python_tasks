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
# user_text = input('Введите текст: ')


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
# def palindrome_02(text):
#     text = text.replace(' ', '')
#     a = text[::-1]
#     if text == a:
#         print('Это палиндром')
#     else:
#         print('Это не палиндром')
#
#
# palindrome(user_text)
# palindrome_02(user_text)

# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами
# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами


# def in_reverse(text):
#     a = (len(text) - 1) // 2
#     if len(text) % 2 == 0:
#         print(f'{text[a+1:len(text)]}{text[:a+1]}')
#     else:
#         print(f'{text[a+1:len(text)]}{text[a]}{text[:a]}')


# user_text = input('Введите текст: ')
# in_reverse(user_text)

# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре


# def number_of_uppercase_characters(text):
#     count = 0
#     for i in text:
#         if i.isupper() is True:
#             count += 1
#     print(count)
#
# user_text_01 = input('Введите текст: ')
# number_of_uppercase_characters(user_text_01)


# 3.6 Безопасный пароль. Пользователь вбивает пароль. Нужно сказать -
# безопасный он или нет. Безопасным считается, если он от 8 символов,
# есть верхний и нижний регистр. А так же цифры. Можеет, при желании, добавить и спец. символы
#
# def check_save_password(user_password):
#     if len(user_password) < 8:
#         print('Слишком короткий пароль')
#     else:
#         uppercase = 0
#         lowercase = 0
#         num = 0
#         for i in user_password:
#

# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего


# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
