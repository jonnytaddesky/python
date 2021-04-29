numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in numbers:
    print(i)

for i in numbers:
    print(i*i)

numbers = range(1, 6)
print(type(numbers))

for i in numbers:
    print(i)

for i in range(6):
    print(i)

for i in range(1, 6):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

numbers = [1, 3, 5, 7, 9]
for i, item in enumerate(numbers):
    numbers[i] *= 2
print(numbers)

name = 'John'

for l in name:
    print(l)

for _ in range(5):
    print('Alarm!')

person = ('John', 'silver', 2)
for item in person:
    print(item)

persons = [('John', 22), ('Valia', 24)]
print(len(persons))

for (name, age) in persons:
    print(f'{name} is {age} years old')

players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801)

for item in players:
    print(item)

players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801)
for item in players.items():
    print(item)

players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801)
for k, v in players.items():
    print(f'{k} has rating {v}')

players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801)
for v in players.values():
    print(v)

# find all pairs sum of which equals 0
list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]
pairs = []

for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))
print(pairs)
