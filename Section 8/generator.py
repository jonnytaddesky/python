import random
import itertools

# def randoms(min, max, n):
#     return [random.randint(min, max) for _ in range(n)]


# for r in randoms(10, 30, 5):
#     print(r)

def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


# for r in randoms(10, 30, 5):
#     print(r)

rand_sequence = randoms(1, 10, 10)
print(rand_sequence)

for r in rand_sequence:
    print(r)

seq = list(randoms(1, 10, 5))
print(seq)
print(seq)
print(seq)

rand_sequence = randoms(1, 10, 10)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)


def randoms(min, max):
    while True:
        yield random.randint(min, max)


rand_sequence = randoms(1, 100000)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)


def read_line_by_line(file):
    """Lazy function (genreation) to read a file line by line"""
    while True:
        line = file.readline()
        if not line:
            break
        yield line


file = open(f'C:\\tmp\\test.txt')
for line in read_line_by_line(file):
    print(line.rstrip())


rand_seq = randoms(1, 10)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)


my_list = [1, 2, 3, 4]
squares = [x**2 for x in my_list]
print(squares)


squares = (x**2 for x in my_list)
print(squares)
for i in squares:
    print(i)
