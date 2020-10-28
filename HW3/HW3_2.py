value = int(input('Enter second value: '))

for i in range(value+1):
    if i % 2 == 0:
        print(f'{i} is EVEN')
    else:
        print(f'{i} is ODD')