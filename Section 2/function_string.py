x = "hello, my name is Artem"


print(len(x))

x[len(x)-1]


x.count('l')

x.capitalize()
print(x)

x.upper()
print(x)


upper_cased = x.upper()
print(upper_cased)


lower_cased = x.lower()
print(lower_cased)


print(upper_cased.isupper())
print(lower_cased.islower())
print(x.isupper())
print(x.islower())


lower_cased.islower()


upper_cased.islower()


print(x.find('l'))
print(x.find('r', 5))
print(x.find('l', 5, 10))
print(x.find('m', 7, 15))
print(x.find('m', 8, 15))


print(x.find('my'))


print('123abc'.isalnum())
print('123abc!'.isalnum())


print('123abc'.isalpha())
print('abc'.isalpha())


print("   ".isspace())
print("".isspace())


empty_string = ""
print(empty_string == "")


empty_string = "   "
print(empty_string.strip(' ') == "")


empty_string = "   "
print(empty_string.strip() == "")


empty_string = ""

if not empty_string:
    print("not empty")
else:
    print("empty")


h = "hello"
print(h.startswith("he"))
print(h.endswith("lo"))


split = h.split('l')
print(type(split))
print(split)
split = h.split('e')
print(split)


data = "12;10;8;10"
print(data.split(';'))
separated_data = data.split(';')
print(separated_data)


python = "python is fun"
print(python.partition('is '))
print(python.partition('not '))


python = "Python is fun, isn't it"
print(python.partition('is'))
