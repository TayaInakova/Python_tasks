# Допустим, всё, что вводит пользователь - валидно.

# Задача 3

cash = int(input('Введите общую сумму зарплаты: '))
a = [0, 25]
b = [0, 10]
c = [0, 3]
d = [0, 1]
if cash > 0:
    for i in a, b, c, d:
        if cash // i[1] != 0:
            i[0] = cash // i[1]
            cash -= i[1] * i[0]


    def declension(num, end: list[str]):
        if num % 10 == 1 and num % 100 != 11:
            return end[0]
        elif (num % 10 == 2 or num % 10 == 3 or num % 10 == 4) and (num % 100 != 12 or num % 100 != 13 or num % 100 != 14):
            return end[1]
        else:
            return end[2]


    word_ending = ["а", "ы", ""]
    nominal = ["ь", "я", "ей"]
    for i in a, b, c, d:
        if i[0] != 0:
            print(f'{i[0]} купюр{declension(i[0], word_ending)} номиналом {i[1]} рубл{declension(i[1], nominal)}')
else:
    print('Зарплаты нет')
