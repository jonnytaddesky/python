# def hello_world():
#     print('Hello World!')

# hello_world()

# hello2 = hello_world
# hello2()


# def hello_world():
#     def internal():
#         print('Hello, World!')
#     return internal

# hello2 = hello_world()
# hello2()


# def say_something(func):
#     func()

# def hello_world():
#     print('Hello, World!')

# say_something(hello_world)


# def log_decorator(func):
#     def wrap():
#         print(f'Calling func {func}')
#         func()
#         print(f'Func {func} finished its work')
#     return wrap

# def hello():
#     print('hello, world!')

# wrapped_by_logger = log_decorator(hello)
# wrapped_by_logger()

# @log_decorator
# def hello():
#     print('hello, world!')

# hello()


# декоратор для замера скорости работы функции
from timeit import default_timer as timer
import math
import time


def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f'Function {func.__name__} took {end-start} for execution')
    return inner


@measure_time
def factorial(num):
    # time.sleep(3)
    print(math.factorial(num))


factorial(5)
