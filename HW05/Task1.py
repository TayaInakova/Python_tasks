# 2. Морской бой

# 0 - пустая клетка
# 1 - клетка с кораблём
# * - мимо
# x - попадание

import random


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


def auto_fill_ships(array, ships):
    for k in range(ships):
        c = random.randint(0, len(array) - 2)
        d = random.randint(1, len(array) - 2)
        while array[c][d + 1] == 1:
            c = random.randint(0, len(array) - 2)
            d = random.randint(1, len(array) - 2)
        array[c][d + 1] = 1


def filling_in_manually(array, ships):
    for u in range(ships):
        vertical = int(
            input(f'Введите координату {u + 1}го корабля по вертикали: '))
        horizontal = int(
            input(f'Введите координату {u + 1}го корабля по горизонтали: '))
        print()
        while array[vertical - 1][horizontal] == 1:
            print('Координаты вне поля, либо уже заняты')
            vertical = int(input('Введите координату корабля по вертикали: '))
            horizontal = int(
                input('Введите координату корабля по горизонтали: '))
            print()
        else:
            array[vertical - 1][horizontal] = 1


def fill_battlefield(array, ships, flag):
    if flag is True:
        filling_in_manually(array, ships)
    else:
        auto_fill_ships(array, ships)


def print_battlefield(array):
    for a in range(len(array)):
        for b in range(len(array[a])):
            print(array[a][b], end='   ')
        print()
    print()


def array_array(array):
    target_array = []
    for e in range(len(array) - 1):
        for j in range(len(array[e])):
            if j != 0:
                target_array.append([e, j])
    return target_array


def player_move(enemy_array, visible_array, win_point):
    print_battlefield(visible_array)
    shot0 = int(input('Введите координату выстрела по вертикали: '))
    shot1 = int(input('Введите координату выстрела по горизонтали: '))
    print()
    if enemy_array[shot0 - 1][shot1] == 1:
        visible_array[shot0 - 1][shot1] = 'x'
        win_point += 1
        print('Попадание!')
        print()
        return win_point
    elif visible_array[shot0 - 1][shot1] != 0:
        print('Вы уже стреляли в эту клетку')
        print()
        return win_point
    else:
        visible_array[shot0 - 1][shot1] = '*'
        print('Мимо!')
        print()
        return win_point


def comp_move(player_array, choice_array, comp_win_point):
    comp_choices = random.choice(choice_array)
    if player_array[comp_choices[0]][comp_choices[1]] == 1:
        player_array[comp_choices[0]][comp_choices[1]] = 'x'
        print_battlefield(player_array)
        comp_win_point += 1
        choice_array.remove(comp_choices)
        print('Попадание!')
        print()
        return comp_win_point
    else:
        player_array[comp_choices[0]][comp_choices[1]] = '*'
        print_battlefield(player_array)
        choice_array.remove(comp_choices)
        print('Мимо!')
        print()
        return comp_win_point


size, count_of_ships, number_of_shells, enemy_ships = 0, 0, 0, 0
win, user_win, comp_win, user1_win, user2_win = 0, 0, 0, 0, 0

type_game = int(input(
    'Выберите тип игры: Игрок - Компьютер (1), Игрок1 - Игрок2 (2), Тренировка меткости (3):  '))

if type_game == 1:  # игрок - комп
    difficulty_level = int(
        input('Задайте уровень сложности (1 - легкий, 2 - средний, 3 - сложный): '))
    if difficulty_level != 1 and difficulty_level != 2 and difficulty_level != 3:
        print('Игра не может быть начата')
    else:
        if difficulty_level == 1:
            count_of_ships = 5
            size = 3
            print('Поле 3х3, 5 кораблей')
        elif difficulty_level == 2:
            count_of_ships = 6
            size = 5
            print('Поле 5х5, 6 кораблей')
        elif difficulty_level == 3:
            count_of_ships = 7
            size = 6
            print('Поле 6х6, 7 кораблей')
    turn = True
    player_field = create_battlefield(size)
    computer_field = create_battlefield(size)
    visible = create_battlefield(size)

    fill_battlefield(player_field, count_of_ships, True)
    fill_battlefield(computer_field, count_of_ships, False)

    player_choice = array_array(player_field)

    while user_win != count_of_ships and comp_win != count_of_ships:
        if turn is True:
            print('Ваш ход:')
            user_win = player_move(computer_field, visible, user_win)
            turn = not turn
        else:
            print('Ходит компьютер:')
            comp_win = comp_move(player_field, player_choice, comp_win)
            turn = not turn
    else:
        if user_win == count_of_ships:
            print(f'Вы выиграли со счётом {user_win}:{comp_win}!')
        else:
            print(f'Вы проиграли со счётом {user_win}:{comp_win}')

elif type_game == 2:  # 2 игрока
    difficulty_level = int(
        input('Задайте уровень сложности (1 - легкий, 2 - средний, 3 - сложный): '))
    if difficulty_level != 1 and difficulty_level != 2 and difficulty_level != 3:
        print('Игра не может быть начата')
    else:
        if difficulty_level == 1:
            count_of_ships = 5
            size = 3
            print('Поле 3х3, 5 кораблей')
        elif difficulty_level == 2:
            count_of_ships = 6
            size = 5
            print('Поле 5х5, 6 кораблей')
        elif difficulty_level == 3:
            count_of_ships = 7
            size = 6
            print('Поле 6х6, 7 кораблей')

    turn = True

    player1_field = create_battlefield(size)
    player2_field = create_battlefield(size)

    vis1 = create_battlefield(size)
    vis2 = create_battlefield(size)

    print('Первый игрок, расставьте, пожалуйста, свои корабли: ')
    print()
    fill_battlefield(player1_field, count_of_ships, True)
    print()

    print('Второй игрок, расставьте, пожалуйста, свои корабли: ')
    print()
    fill_battlefield(player2_field, count_of_ships, True)
    print()

    while user1_win != count_of_ships and user2_win != count_of_ships:
        if turn is True:
            print('Ходит первый игрок:')
            user1_win = player_move(player2_field, vis1, user1_win)
            turn = not turn
        else:
            print('Ходит второй игрок:')
            user2_win = player_move(player1_field, vis2, user2_win)
            turn = not turn
    else:
        if user1_win == count_of_ships:
            print(f'Выиграл первый игрок со счётом {user1_win}:{user2_win}!')
        else:
            print(f'Выиграл второй игрок со счётом {user2_win}:{user1_win}')

elif type_game == 3:  # Тренировка меткости
    diff_level = int(input('Задайте уровень сложности (1 - легкий, 2 - средний, 3 - сложный): '))
    if diff_level != 1 and diff_level != 2 and diff_level != 3:
        print('Игра не может быть начата')
    else:
        if diff_level == 1:
            number_of_shells = 10
            enemy_ships = 3
            size = 4
            win = 0
            print('3 вражеских корабля, 10 снарядов')
            print()
        elif diff_level == 2:
            number_of_shells = 9
            enemy_ships = 4
            size = 4
            win = 0
            print('4 вражеских корабля, 9 снарядов')
            print()
        elif diff_level == 3:
            number_of_shells = 8
            enemy_ships = 5
            size = 4
            win = 0
            print('5 вражеских кораблей, 8 снарядов')
            print()

    comp_field = create_battlefield(size)
    auto_fill_ships(comp_field, enemy_ships)
    visible_field = create_battlefield(size)
    for i in range(number_of_shells):
        win = player_move(comp_field, visible_field, win)
    print(f'Выстрелов: {number_of_shells}')
    print(f'Попаданий: {win}')
    print()
