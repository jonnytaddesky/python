import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi*self.radius**2

    def get_perimeter(self):
        return self.radius*2*math.pi


c = Circle(10)
print(c.get_area())
print(c.get_perimeter())
