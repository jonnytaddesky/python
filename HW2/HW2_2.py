import math
x1 = int(input('Введите координату х1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату х2: '))
y2 = int(input('Введите координату y2: '))

result = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 3)
print(f'Расстояние между точками: {result}')
