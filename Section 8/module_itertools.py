import itertools as it

# iterable = [1, 2, 3]

# iterator = iter(iterable)  # будет вызван метод __iter__()
# print(type(iterator))

# print(next(iterator))  # будет вызван метод __next__()

# print(next(iterator))
# print(next(iterator))

# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)

# even_numbers = it.count(0, 2)
# print(even_numbers)
# # for x in even_numbers:
# #     print(x)
# print(list(next(even_numbers) for _ in range(5)))


# print(list(zip(it.count(), ['a', 'b', 'c'])))


def print_iterable(iterable, end=None):
    for x in iterable:
        if end:
            print(x, end=end)
        else:
            print(x)


# ones = it.repeat(1, 5)
# print_iterable(ones, ' ')
# print()
# print(list(map(pow, range(10), it.repeat(2))))

for _ in it.repeat(None, 10000):
    pass
    # do something это быстрее

for _ in range(10000):
    pass
    # compute это медленнее

# pos_neg_ones = it.cycle([1, -1])
# print(list(next(pos_neg_ones) for _ in range(10)))

# letters = it.cycle(['A', 'B', 'C'])
# print(list(next(letters) for _ in range(10)))

# print(list(it.accumulate([1, 2, 3, 4, 5])))
# print(list(it.accumulate(['A', 'B', 'C', 'D'])))

# print(list(it.accumulate([3, 1, 4, 2, 7, 3, 8, 5, 8], max)))

# print(list(it.chain('ABC', 'DEF')))

# print(list(it.chain.from_iterable(['ABC', 'DEF'])))

# print(list(it.chain([1, 2, 3], [4, 5, 6], [7, 8, 9])))

# print(list(it.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5])))

# print(list(it.takewhile(lambda x: x < 3, [1, 2, 3, 4, 5])))

print(list(it.filterfalse(lambda x: x % 2 == 0, range(10))))

# iterable = iter([1, 2, 3])
# print_iterable(iterable, ' ')
# print("\nIterable is exausted")
# print_iterable(iterable, ' ')
# print()
# iterable1, iterable2 = it.tee([1, 2, 3], 2)
# print_iterable(iterable1, ' ')
# print("\nIterable is exausted")
# print_iterable(iterable2, ' ')


names = ['Carlsen', 'Caruana', 'Mameduarov', 'Ding', 'Givi']
ratings = [2842, 2822, 2801, 2797, 2780]

for name, rating in zip(names, ratings):
    print(f'{name}:{rating}')

print(list(zip(names, ratings)))
players = dict(zip(names, ratings))
print(players)

names = ['Carlsen', 'Caruana', 'Mameduarov', 'Ding', 'Givi', 'Kramnik']
ratings = [2842, 2822, 2801, 2797, 2780]
# players = dict(zip(names, ratings))
# print(players)
players = dict(it.zip_longest(names, ratings, fillvalue=0))
print(players)

lst = [1, 2, 1, 2, 2, 3, 3, 2]
for key, grp in it.groupby(sorted(lst)):
    print('{}:{}'.format(key, list(grp)))

forecast = [{'humidity': 20, 'temperature': 78, 'wind': 7},
            {'humidity': 50, 'temperature': 61, 'wind': 10},
            {'humidity': 100, 'temperature': 81, 'wind': 5},
            {'humidity': 90, 'temperature': 62, 'wind': 15},
            {'humidity': 20, 'temperature': 84, 'wind': 19},
            {'humidity': 0, 'temperature': 66, 'wind': 28},
            {'humidity': 100, 'temperature': 87, 'wind': 12},
            {'humidity': 0, 'temperature': 68, 'wind': 14},
            {'humidity': 90, 'temperature': 86, 'wind': 4},
            {'humidity': 50, 'temperature': 68, 'wind': 0}
            ]


# def group_sorted(iterable, key=None):
#     return it.groupby(sorted(iterable, key=key), key=key)


# grouped_data = group_sorted(forecast, key=lambda x: x['humidity'])
# for key, grp in grouped_data:
#     print('{}:{}'.format(key, list(grp)))

# even_numbers = it.count(0, 2)
# print([x for x in range(20) if x % 2 == 0])
# print(list(it.islice(even_numbers, 2, 10, 2)))


# even_numbers = it.count(0, 2)
# print(list(it.islice(even_numbers, 4)))


# even_numbers = it.count(0, 2)
# print(list(it.islice(even_numbers, 2, 4)))


# pin = [7, 5, 2, 8]
# print(list(it.permutations(pin)))


# ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# suits = ['H', 'D', 'C', 'S']

# lst = list(it.product(ranks, suits))
# print(lst)

# print(list(it.combinations(lst, 2)))

print(list(it.combinations('ABCD', 2)))
