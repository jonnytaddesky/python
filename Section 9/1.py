# import pyscreenshot
# import validators

# scrennshot = pyscreenshot.grab()
# scrennshot2 = pyscreenshot.grab(bbox=(0, 0, 1920, 1080))

# print(validators.email("johnsmith20632@gmail.com"))

# print(validators.email("johnsmith20632gmail.com"))


# print(validators.ipv4('1.1.1.255'))

# arr = [True, False, True]

# one = all(arr + list(map(lambda x: not x, arr)))
# two = any(list(filter(lambda x: x, arr)) + [True, not False, True])

# print(one or two)

# from itertools import filterfalse

# arr = range(0, 10)
# arr = list(filterfalse(lambda x: x % 2, arr))

# for i in range(0, 5, 2):
#     arr.pop()

# print(arr)

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
# plt.show()

# z = [1, 1, 1, 1, 1, 2, 18, 29, 4, 9, 17]

z = [3]


def max_number(z):
    if len(z) > 1:  # если список состоит из одного элемента, выводим этот элемент
        if z[0] >= z[1]:  # сравниваем 1ый и 2ой элементы списка
            # удаляем меньший элемент, т.к. он больше не учавствует в гонке
            z.pop(1)
            return(max_number(z))
        else:
            z.pop(0)
            return(max_number(z))
    else:
        return(z)  # после удаления всех наименьших,
    # должен остаться список из одного элемента, но список почему-то полностью чистится


print('Max number in list is - ', max_number(z))
