# Допустим, всё, что вводит пользователь - валидно.

# Задача 3

x = int(input('Введите координату точки A по оси х: '))
y = int(input('Введите координату точки A по оси y: '))
if x > 0 and y > 0:
    print(f'Точка А ({x},{y}) расположена в 1й четверти')
elif x < 0 and y > 0:
    print(f'Точка А ({x},{y}) расположена в 2й четверти')
elif x < 0 and y < 0:
    print(f'Точка А ({x},{y}) расположена в 3й четверти')
elif x > 0 and y < 0:
    print(f'Точка А ({x},{y}) расположена в 4й четверти')
