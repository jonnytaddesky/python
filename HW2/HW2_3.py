chikens = int(input('Введите колличество кур: '))
pigs = int(input('Введите колличество свиней: '))
cows = int(input('Введите колличество коров: '))

chicken_legs = 2
pig_and_cow_legs = 4

all_legs = chikens * chicken_legs + (pigs + cows) * pig_and_cow_legs
print(f'Всего ног всех животных: {all_legs}')