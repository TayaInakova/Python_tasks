# 3.12 Вводим с клавиатуры строку. Необходимо вывести строку,
# где развернём подстроку между первой и последней буквой "о"
# из исходной строки. Если она только одна или её нет - то сообщить,
# что буква "о" - одна или не встречается.


def the_main_fish(text, letter):
    a = None
    b = None
    if text.find(letter) >= 0:
        a = text.find(letter)
        if text.rfind(letter) > a:
            b = text.rfind(letter)
            c = text[b:a:-1]
            print(f'{text[0:a]}{c}{text[b:len(text)]}')
        else:
            print('Искомая буква только одна')
    else:
        print('В строке нет нужной буквы')


valume = input('Введите произвольный текст: ')
s = 'о'
the_main_fish(valume, s)
