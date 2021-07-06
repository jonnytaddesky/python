counter_sticks = int(input('Общее колличество палочек: '))
player_number = 1

while counter_sticks > 0:
    choice = int(
        input(f'Сколько возьмете палочек? Осталось палочек {counter_sticks}: '))
    if choice > 3 or choice < 1:
        print(f"Вы взяли {choice} палочек. Дозвонлено взять 1, 2 или 3")
    elif choice == 3 and counter_sticks < 3:
        print(
            f"Вы взяли {choice} палочек. Осталось {counter_sticks}. Дозвонлено взять 1, 2")
        continue
    elif choice >= 2 and counter_sticks < 2:
        print(
            f"Вы взяли {choice} палочек. Осталось {counter_sticks}. Дозвонлено взять 1")
        continue

    counter_sticks -= choice
    print(f'Игрок номер {player_number} взял {choice} палочек')

    if counter_sticks <= 0:
        print(f'Игрок {player_number} проиграл.')

    player_number = 1 if player_number == 2 else 2
