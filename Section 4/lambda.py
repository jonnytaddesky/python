# def square(*args):
#     return [x*x for x in args]

# result = square(1,2,3,4,5)
# print(result)


# def triple(*args):
#     return [x*3 for x in args]

# result = triple(1,2,3,4,5)
# print(result)


# def square(number):
#     return number*number

# numbers = [1,2,3,4,5]

# result = map(square, numbers)

# for x in map(square, numbers):
#     print(x)

# print(type(result))

# print(list(map(square, numbers)))


# def is_adult(age):
#     return age >= 18

# ages = [14, 18, 21, 16, 30]

# filter(is_adult, ages)

# print(list(filter(is_adult, ages)))


ages = [14, 18, 21, 16, 30]

print(list(filter(lambda age: age >= 18, ages)))

# multiplayer = lambda x, y: x * y

# print(multiplayer(2, 3))


