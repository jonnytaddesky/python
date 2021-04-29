# greeting = 'Hello from the global scope'

# def greet():
#     greeting = 'Hello from enclosing scope'

#     def nested():
#         greeting = 'Hello from local scope'
#         print(greeting)
#     nested()

# greet()
# print(greeting)


greeting = 'Hello from the global scope'


def greet(greeting):
    print(f'Greet in func1: {greeting}')

    greeting = 'Hello from enclosing scope'

    print(f'Greet in func2: {greeting}')

    def nested():
        greeting = 'Hello from local scope'
        print(greeting)
    nested()


greet('test')
print(greeting)
