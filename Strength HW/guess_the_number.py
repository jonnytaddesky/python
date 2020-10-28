from random import randint

number_pc = randint(1, 50)
tries = 1
trye = 6

while tries <= 6:
    number_man = int(input(f'Угадай число от 1 до 50 которое я загадал. У тебя осталось {trye} попыток. Попытка № {tries}: '))
    if number_man == number_pc:
        print(f'Число отгадано. Это число {number_pc}')
        break
    elif number_man < number_pc:
        print('Число меньше загаданого')
        tries += 1
        trye -= 1
    elif number_man > number_pc:
        print('Число больше загаданого')
        tries += 1
        trye -= 1
else:
    print(f'Попытки кончились. Мое число {number_pc}')