# greeting = 'Hello, World!'

# chars = []

# for l in greeting:
#     chars.append(l)

# print(chars)

# chars = [l for l in greeting]
# print(chars)

# chars = [l for l in 'bla-bla-bla']
# print(chars)

# numbers = [x for x in range(0, 11)]
# print(numbers)

# number = [x*x for x in range(0, 11)]
# print(number)

# values = [n*n for n in range(0, 11) if n % 2 != 0]
# print(values)

# len_in_centimeters = [12, 10, 54, 124, 65]

# len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_centimeters]
# print(len_in_inches)

# ratings = [2485, 2580, 2480, 2600, 2482, 2520]
# titles = ['GM' if x >= 2500 else 'MM' for x in ratings]
# print(titles)

list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]

pairs = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))
print(pairs)


pairs = [(x, y) for x in list1 for y in list2 if x + y == 0]

print(pairs)
