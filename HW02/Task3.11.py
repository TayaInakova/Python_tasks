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


def right_check(text):
    text = text.replace(',', '.')
    if text.count('.') > 1:
        print('Ты втираешь мне какую-то дичь')
    else:
        for k in text:
            if k != '.' and not k.isdigit():
                print('Ты втираешь мне какую-то дичь')
                break
        else:
            if text != str(float(text)):
                print('Число целое')
            else:
                print('Число дробное')


number = input('Введите строку: ')
print(is_realy_float(number))
right_check(number)
