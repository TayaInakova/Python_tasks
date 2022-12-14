# 1) Камень - ножницы - бумага
# 2) Морской бой. (1 поле. 1 корабль. Игрок бьёт по компьютеру)


# 1. Камень-ножницы-бумага

# from random import randint

# number_of_rounds = int(input('Введите колчество раундов (0 - для выхода): '))
# if number_of_rounds > 0:
#     defeat = 0
#     win = 0
#     for i in range(number_of_rounds):
#         comp_choice = randint(1, 3)
#         player_choice = int(input('Выберите камень, ножницы или бумагу (1, 2 или 3) или 0 - для выхода: '))
#         if player_choice == 0:
#             print('Ок, больше не играем')
#             print(f'Побед: {win}')
#             print(f'Поражений: {defeat}')
#             break
#         else:
#             if player_choice != 1 and player_choice != 2 and player_choice != 3:
#                 print('Вы зря потратили раунд.')
#                 print()
#             else:
#                 if comp_choice == player_choice:
#                     print('И вы и компьютер выбрали одно и то же. Ничья!')
#                     print()
#                 elif comp_choice == 1:
#                     if player_choice == 2:
#                         print('Вы выбрали ножницы, компьютер загадал камень. Мне очень жаль, но вы проиграли...')
#                         defeat += 1
#                         print()
#                     elif player_choice == 3:
#                         print('Вы выбрали бумагу, компьютер загадал камень. Вы победили!')
#                         win += 1
#                         print()
#                 elif comp_choice == 2:
#                     if player_choice == 1:
#                         print('Вы выбрали камень, компьютер загадал ножницы. Вы победили!')
#                         win += 1
#                         print()
#                     elif player_choice == 3:
#                         print('Вы выбрали бумагу, компьютер загадал ножницы. Мне очень жаль, но вы проиграли...')
#                         defeat += 1
#                         print()
#                 elif comp_choice == 3:
#                     if player_choice == 1:
#                         print('Вы выбрали камень, компьютер загадал бумагу. Мне очень жаль, но вы проиграли...')
#                         defeat += 1
#                         print()
#                     elif player_choice == 2:
#                         print('Вы выбрали ножницы, компьютер загадал бумагу. Вы победили!')
#                         win += 1
#                         print()
#     else:
#         print('Игра завершилась со счётом:')
#         print(f'Побед: {win}')
#         print(f'Поражений: {defeat}')
# elif number_of_rounds == 0:
#     print('Ок, игры не будет')
# elif number_of_rounds < 0:
#     print('Некорректный ввод')



#         for i in range(4):
#             speedboat = []
#             coordinate = [randint(1, 10), randint(1, 10)]
#             speedboat.append(coordinate)
#             for i in range(len(speedboat)):
#                 array[(speedboat[i][0]) - 1][(speedboat[i][1])] = 1
#             print(speedboat)
#
#
# def players_move(array, player):
#     if player == 1:
#         print('Ходит первый игрок')
#
#     elif player == 2:
#         print('Ходит второй игрок')
#         while player == 2:
#             point = input('Введите через запятую координаты выстрела: ').split(',')
#
#             if array[point[0] - 1][point[1]] == 1:
#                 print('Попадание!')
#             else:
#                 print('Мимо!')
#                 player = 1
#                 break
#
# def comp_shot(user_array, num_of_shot):
#     for k in range(num_of_shot):
#         i = randint(0, len(user_array) - 2)
#         j = randint(1, len(user_array) - 2)
#         if user_array[i][j + 1] == '1':
#             user_array[i][j + 1] = 'x'
#             print_battlefield(user_array)
#             print('Ваш корабль подбит')
#         else:
#             user_array[i][j + 1] = '*'
#             print_battlefield(user_array)
#             print('Промах!')
#
