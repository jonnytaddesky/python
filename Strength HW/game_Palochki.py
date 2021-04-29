counter_sticks = int(input('Общее колличество палочек: '))
player_number = 1

while counter_sticks > 0:
    choise = int(
        input(f'Сколько возьмете палочек? Осталось палочек {counter_sticks}: '))
    if choise > 3 or choise < 1:
        print(f"Вы взяли {choise} палочек. Дозвонлено взять 1, 2 или 3")
        continue

    counter_sticks -= choise
    print(f'Игрок номер {player_number} взял {choise} палочек')

    if counter_sticks <= 0:
        print(f'Игрок {player_number} проиграл.')

    player_number = 1 if player_number == 2 else 2
