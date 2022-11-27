# Допустим, всё, что вводит пользователь - валидно.

# Задача 3

multivalued = int(input('Введите многозначное число: '))
validation_check = None
ascending_order = True
while multivalued // 10 != 0:
    if validation_check is None:
        validation_check = multivalued % 10
        multivalued = multivalued // 10
    elif multivalued % 10 <= validation_check:
        validation_check = multivalued % 10
        multivalued = multivalued // 10
    else:
        ascending_order = False
        break
if ascending_order is True:
    print('последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию.')
else:
    print('Последовательнось цифр не упорядочена')
