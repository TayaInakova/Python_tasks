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


# num = int(input('Введите число в десятичной системе: '))
# num1 = int(input('Введите основание системы счисления: '))
# transfer(num, num1)


def right_16_convert(text):
    f = ''
    right_16 = 'ABCDEF'
    if text > 0:
        while text > 0:
            temporary = text % 16
            if temporary > 9:
                a = temporary % 10
                temporary = right_16[a]
            text = text // 16
            f += str(temporary)
        text = f[::-1]
        print(f"Шестнадцатиричное представление заданного числа: {text}")
    elif text == 0:
        print("Перевод нуля в любую систему счисления даст ноль.")
    else:
        print("Сложное...")


user_input = int(input('Введите число: '))
right_16_convert(user_input)
