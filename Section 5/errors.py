# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as ex:
#         print(f'an error occured: {ex}')
#     except:
#         print('unknow error occured!')

# print(divide(4,2))
# divide(4,0)

# divider = input()
# divide(4, divider)

# file = None
# try:
#     file = open(r'C:\tmp\abracadabra.txt')
#     data  = file.read()
# except FileNotFoundError as ex:
#     print(f'Error has occured. Discription: {ex.strerror}')
# else:
#     print('возможно else')
# finally:
#     print('Finally')
#     if file:
#         file.close()

# print('doing some work here')


def get_int():
    while True:
        try:
            reply = int(input('Enter a number: '))
            return reply
        except:
            print('Not a number! Try again.')
            continue


get_int()
