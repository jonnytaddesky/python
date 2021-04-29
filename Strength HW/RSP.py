from random import randint

choise_pc_dict = {
    1: 'R',
    2: 'S',
    3: 'P'
}

games = True

while games:
    choise_pc = randint(1, 3)
    choise_guest = input(
        'Введите свой вариант r - камень, s - ножницы, p - бумага: ')
    if choise_guest not in ['r', 's', 'p']:
        print('Введите корректные данные!')
        continue
    if choise_guest == 'r' and choise_pc == 1:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Ничья!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 's' and choise_pc == 1:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Вы проиграли!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 'p' and choise_pc == 1:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Вы выиграли!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 'r' and choise_pc == 2:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Вы выиграли!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 's' and choise_pc == 2:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Ничья!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 'p' and choise_pc == 2:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Вы проиграли!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 'r' and choise_pc == 3:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Вы проиграли!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 's' and choise_pc == 3:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Вы выиграли!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'
    elif choise_guest == 'p' and choise_pc == 3:
        print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
        print('Ничья!')
        games = input('Продолжить игру? Введите [y/n]: ') == 'y'


# choise_pc_dict = {
#     1: 'R',
#     2: 'S',
#     3: 'P'
# }

# games_continues = True

# while games_continues:
#     choise_pc = randint(1, 3)
#     choise_guest = input('Введите свой вариант R - камень, S - ножницы, P - бумага: ')
#     if choise_guest not in ['R', 'S', 'P']:
#         print('Введите корректные данные!')
#         continue

#     winning_combinations = [('P', 'R'), ('R', 'S'), ('S', 'P')]

#     if choise_guest == choise_pc:
#         print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
#         print('Ничья')

#     elif (choise_guest , choise_pc) in winning_combinations:
#         print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
#         print('Вы выиграли!')

#     else:
#         print(f'Выбор компьютера {choise_pc_dict.get(choise_pc)}')
#         print('Вы проиграли!')

#     games_continues = input('Продолжить игру? Введите [y/n]: ') == 'y'
