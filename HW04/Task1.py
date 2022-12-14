# 2. Морской бой

# 0 - пустая клетка
# 1 - клетка с кораблём
# * - мимо
# x - попадание

from random import randint

size, number_of_shells, number_of_shot, enemy_ships, win = 4, 0, 0, 0, 0
difficulty_level = int(input('Задайте уровень сложности (1 - легкий, 2 - средний, 3 - сложный): '))
if difficulty_level != 1 and difficulty_level != 2 and difficulty_level != 3:
    print('Игра не может быть начата')
else:
    if difficulty_level == 1:
        number_of_shells = 10
        enemy_ships = 3
        print('3 вражеских корабля, 10 снарядов')
    elif difficulty_level == 2:
        number_of_shells = 9
        enemy_ships = 4
        print('4 вражеских корабля, 9 снарядов')
    elif difficulty_level == 3:
        number_of_shells = 8
        enemy_ships = 5
        print('5 вражеских кораблей, 8 снарядов')


    def create_battlefield(field_size):
        new_battlefield = []
        for n in range(field_size + 1):
            new_battlefield.append([[]])
            for m in range(field_size):
                new_battlefield[n].append([])
        count = 1
        for q in range(field_size + 1):
            for w in range(field_size + 1):
                if count > field_size:
                    count = 0
                if q == field_size:
                    new_battlefield[q][w] = count
                    count += 1
                elif w == 0:
                    new_battlefield[q][w] = count
                    count += 1
                else:
                    new_battlefield[q][w] = 0
        return new_battlefield


    def fill_battlefield_ships(array, ships):
        for k in range(ships):
            c = randint(0, len(array) - 2)
            d = randint(1, len(array) - 2)
            array[c][d + 1] = 1


    def print_battlefield(array):
        for a in range(len(array)):
            for b in range(len(array[a])):
                print(array[a][b], end='   ')
            print()
        print()


    comp_field = create_battlefield(size)
    fill_battlefield_ships(comp_field, enemy_ships)
    visible_field = create_battlefield(size)
    print_battlefield(visible_field)
    for i in range(number_of_shells):
        shot0 = int(input('Введите координату выстрела по вертикали: '))
        shot1 = int(input('Введите координату выстрела по горизонтали: '))
        if comp_field[shot0][shot1] == 1:
            visible_field[shot0 - 1][shot1] = 'x'
            print_battlefield(visible_field)
            win += 1
            number_of_shot += 1
            print('Попадание!')
            print()
        elif visible_field[shot0 - 1][shot1] == 'x' or visible_field[shot0 - 1][shot1] == '*':
            print_battlefield(visible_field)
            number_of_shot += 1
            print('Вы уже стреляли в эту клетку')
            print()
        else:
            visible_field[shot0 - 1][shot1] = '*'
            print_battlefield(visible_field)
            number_of_shot += 1
            print('Мимо!')
            print()
    print(f'Выстрелов: {number_of_shot}')
    print(f'Попаданий: {win}')
