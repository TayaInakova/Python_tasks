# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

def is_realy_float(x):
    x = x.replace(',', '.')
    try:
        float(x)
        if x == str(float(x)):
            return 'Это дробное число'
        else:
            return 'Нет, это целое число'
    except ValueError:
        return 'Это вообще не число'


number = input('Введите строку: ')
print(is_realy_float(number))
