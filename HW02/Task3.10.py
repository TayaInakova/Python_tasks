# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

def transfer(number, radix):
    f = ''
    if radix > 0:
        if number > 0:
            while number > 0:
                temporary = number % radix
                number = number // radix
                f += str(temporary)
            number1 = int(f[::-1])
            print(f"{radix}-ичное представление заданного числа: {number1}")
        elif number == 0:
            print("Перевод нуля в любую систему счисления даст ноль.")
        else:
            print("Сложное...")
    else:
        print("Идея отрицательных систем счисления распространения не нашла. Не только широкого, но и почти никакого.")


num = int(input('Введите число в десятичной системе: '))
num1 = int(input('Введите основание системы счисления: '))

transfer(num, num1)
