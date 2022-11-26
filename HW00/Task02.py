#  Допустим, всё, что вводит пользователь - валидно.

# Задача 2

def Check(x, y, z):
    if not (x or y or z) == (not x and not y and not z):
        result = True
        print(f'{x}, {y}, {z} - {result}')
    else:
        result = False
        print(f'{x}, {y}, {z} - {result}')


Check(True, True, True)
Check(False, True, True)
Check(True, False, True)
Check(True, True, False)
Check(False, False, True)
Check(True, False, False)
Check(False, True, False)
Check(False, False, False)
