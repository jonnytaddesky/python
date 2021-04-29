limit = int(input('Enter the limit: '))

summ = 0
for i in range(limit+1):
    if i % 3 == 0 or i % 5 == 0:
        summ += i
print(summ)


summ = sum([x for x in range(limit+1) if x % 3 == 0 or x % 5 == 0])

print(summ)
