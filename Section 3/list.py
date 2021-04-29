int_list = [1, 2, 3]


mixes_list = [1, 2.0, 'string']


len(int_list)


print(int_list[0])
print(int_list[-1])


print(int_list[1:])


names1 = ['John', 'Bob', 'Alice']
names2 = ['Tracy', 'Elijah', 'Mason']

names_combined = names1 + names2
print(names_combined)


names1[0] = 'Laim'
print(names1)


names1.append('William')
names1.append('James')
print(names1)


popped = names1.pop()
print(popped)
print(names1)


names1.pop(0)
print(names1)


names1.append('Jamaes')
names1.sort()
print(names1)


letter = ['ac', 'ab', 'aa']
letter.sort()
print(letter)


letters = ['abc', 'a', 'ab']
letters.sort(key=len)
print(letters)


letters = ['abc', 'a', 'ab']
letters.sort()
print(letters)


numbers = [3, 2, 8, 5, 0, 3, 4, 1, 1]
print(numbers)
numbers.sort()
print(numbers)


numbers = [3, 2, 8, 5, 0, 3, 4, 1, 1]
numbers.reverse()
print(numbers)


numbers.sort(reverse=True)
print(numbers)


numbers.insert(1, 22)
print(numbers)


print(numbers.index(5))


# print(numbers.index(42))


print(numbers.count(3))


copy = numbers.copy()
print(copy)


numbers.clear()
print(numbers)
