file = open('sample.txt')
file


data = file.read()
print(type(data))
print(data)


print(data)


print(file.read())


file.seek(0)
print(file.read())


file.seek(0)


lines = file.readlines()
print(type(lines))
print(lines)


print(len(lines))


sample_file = open(r"C:\Users\Artem\JupyterRoot\sample.txt")

# or open with double back slasher file = open(r'C:\\User\\Artem\\JupyterRoot\\sample.txt')
#  on linux, we use slashes, so there`s no need r'C:'
#  file = open (/Users/Artem/JupyterRoot/sample.txt)


file.close()
sample_file.close()


print(file.closed)
print(sample_file.closed)


with open('sample.txt') as sample_file:
    sample_data = sample_file.read()


print(sample_data)


# with open('sample.txt', mode='w') as sample_file:
#     data = sample_file.read()


with open('sample.txt', mode='a') as sample_file:
    sample_file.write('Eric;7639')


with open('sample.txt', mode='r') as sample_file:
    print(sample_file.read())


with open('sample.txt', mode='r+') as sample_file:
    sample_file.seek(0, 2)
    sample_file.write('\nToub;5627')
    sample_file.seek(0)
    print(sample_file.read())


with open('abracadabra.txt', mode='w+') as spell_file:
    spell_file.write('abra-abra-abra-cadabra')
    spell_file.seek(0)
    print(spell_file.read())
