import random


# def randoms(min, max, n):
#     return [random.randint(min, max) for _ in range(n)]


# for r in randoms(10, 30, 5):
#     print(r)

def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


for r in randoms(10, 30, 5):
    print(r)

rand_sequence = randoms(1, 10, 10)
print(rand_sequence)

for r in rand_sequence:
    print(r)

seq = list(randoms(1, 10, 5))
print(seq)
print(seq)
print(seq)
