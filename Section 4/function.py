# def greeting():
#     '''
#     DOCSTRING: Information about the function
#     INPUT: no input...
#     OUTPUT: Hello!
#     '''
#     print('Hello!')

# greeting()

# help(greeting)

# def print_name(name):
#     print(name)

# print_name('Artem')


# def print_name(name='Default'):
#     print(name)

# # print_name()

# result = print_name()
# print(result)
# print(type(result))


# def get_greeting(name):
#     return 'Hello ' + name

# greeting = get_greeting('Artem')

# print(greeting)

# def get_sum(a, b):
#     return a + b

# summ = get_sum(10, 2)
# print(summ)

# def is_adult(age):
#     return age >= 18

# is_adult = is_adult(20)
# print(is_adult)


# def is_palindrom(text):
#     return text == text[::-1]

# print(is_palindrom('aabaa'))

# print(is_palindrom('aabba'))


# def calc_taxes(p1, p2, p3):
#     return sum((p1, p2, p3)) * 0.06

# print(calc_taxes(10, 20, 30))

# def calc_taxes(p1, p2, p3, p4):
#     return sum((p1, p2, p3, p4)) * 0.06

# print(calc_taxes(10, 20, 30, 40))

# def calc_taxes(*args):
#     for x in args:
#         print(f'Got payment = {x}')
#     return sum(args) * 0.06

# print(calc_taxes(10, 20,30,40,50,60,70,80))


def save_players(**kwargs):
    for k, v in kwargs.items():
        print(f'Player {k} has rating {v}')

save_players(Carlsen=2800, Giri=2780)


# def func_important(a, b, c, d, *args, **kwargs)