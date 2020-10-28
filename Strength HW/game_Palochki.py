# counter_palochek = int(input('Введите колличество палочек: '))

# while counter_palochek > 0:
#     choise_1st = int(input('Игрок 1, введите колличество палочек, которые вы заберете (от 1 до 3):'))
#     counter_palochek -= choise_1st
#     if counter_palochek == 0:
#         print('Первый игрок проиграл')
#         break
#     else:
#         print(counter_palochek)
#     choise_2nd = int(input('Игрок 2, введите колличество палочек, которые вы заберете (от 1 до 3):'))
#     counter_palochek -= choise_2nd
#     if counter_palochek == 0:
#         print('Второй игрок проиграл')
#         break
#     else:
#         print(counter_palochek)

# palayer_turn = 1
    
# while counter_palochek > 0:
#     choise_1st = int(input(f'Сколько палочек возьмете? Осталось {counter_palochek}: '))
#     if choise_1st < 1 or choise_1st > 3:
#         print(f'Вы повытались взять {choise_1st}. Дозволено взять 1, 2, 3.')
    
#     counter_palochek -= choise_1st
#     print(f'Взято палочек: {choise_1st}\n')

#     if counter_palochek <= 0:
#         print(f'У нас нету больше палочек в игре. Игрок {palayer_turn} проиграл')
    
#     palayer_turn = 1 if palayer_turn == 2 else 2


counter_palochek = int(input('Введите колличество палочек: '))
player_turn = 1

def can_take(sticks):
    return sticks >= 1 and sticks <= 3

def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2

def end_of_game(sticks):
    return counter_palochek <= 0

while (not end_of_game(counter_palochek)):
    pass