# print(abs(-1))

# print(max(1,2,3,4,5))

# print(min([1,2,3,4,5]))

# print(pow(2, 8))

# print(round(3.37, 1))

# print(sum([1,2,3,4,5]))

# h = hex(42)
# print(f'16 ричная система {h}')
# o = oct(42)
# print(f'8 ричная система {o}')
# b = bin(42)
# print(f'2 ичная система {b}')

# all_true1 = all([True, True, True])
# all_true2 = all([True, False, True])

# print(all_true1)
# print(all_true2)

# players = [('Carlsen', 2842), ('Caruana', 2822), ('Mamedyarov', 2801), ('Giri', 2780)]
# print(all(rating > 2700 for _, rating in players)) # fasters, если первый false значит сразу false
# print(all([rating > 2700 for _, rating in players])) # проходит по цыклу, а потом уже ищет

# any_true1 = any([False, False, True])
# any_true2 = any([False, False, False])

# print(any_true1)
# print(any_true2)


# players = [('Carlsen', 2842), ('Caruana', 2822), ('Mamedyarov', 2801), ('Giri', 2780)]
# print(any(rating < 2790 for _, rating in players))

# letters = 'abcd'
# numbers = (10, 20 ,30)

# zipped = zip(letters, numbers)
# print(type(zipped))
# print(zipped)

# zipped_list = list(zipped)
# print(zipped_list)

# names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Giri']
# ratings = [2842, 2822, 2801, 2780]

# players = dict(zip(names, ratings))
# print(players)

# reply = input()
# print(reply)


code = ord('a')
print(code)

c = chr(code)
print(c)

[print('', x, end='\t') for x in "Hello World"]
print()
[print(ord(x), end='\t') for x in "Hello World"]
print()
