import math


class Shape:

    def __init__(self):
        print('Shape created')

    def draw(self):
        # print('Drawing a shape')
        raise NotImplementedError('Can`t instantiate an abstract class')

    def area(self):
        # print('Calc area')
        raise NotImplementedError('Can`t instantiate an abstract class')

    def perimeter(self):
        # print('Calc perimeter')
        raise NotImplementedError('Can`t instantiate an abstract class')


shape = Shape()
print(shape.draw())


class Rectangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self)

        self.width = width
        self.height = height

        print('Rectangle created')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        return f'Drawing rectangle with width = {self.width} and with height = {self.height}'


class Triangle(Shape):

    def __init__(self, a, b, c):
        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c

        print('Triangle created')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def draw(self):
        return f'Drawing triangle with sides = {self.a}, {self.b}, {self.c}'


rect = Rectangle(10, 20)
# print(rect.area())
# print(rect.perimeter())
# print(rect.draw())

triangle = Triangle(3, 4, 5)
# print(triangle.draw())
# print(triangle.area())
# print(triangle.perimeter())

for shape in [rect, triangle]:
    print(shape.draw())
