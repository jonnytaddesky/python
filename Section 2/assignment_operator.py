print(2 > 1)
print(2 < 1)
print(2 == 1)

result = 2 > 1
print(type(result))
print(result)

print(2 > 2)
print(2 >= 2)
print(3 >= 2)
print(3 >= 4)

print(2 < 3)
print(3 < 2)
print(3 <= 3)
print(3 <= 2)
print(3 <= 4)

print(1 == 1)

# 1 = 1

print(1 != 1)

print(2 != 1)

print("string" == 'string')
print("string" == "another string")
print('string' == 'String')

x = 'String'
y = 'string'
print(x.lower() == y.lower())

print(1 < 3 > 2)

print(1 < 2 and 2 < 3)

print(1 > 2 and 2 < 3)

print(1 > 2 or 2 < 3)

print(1 > 2 or 2 > 3)

is_admin = False
if not is_admin:
    print('not an admin')
    
if is_admin == False:
    print('not an admin')