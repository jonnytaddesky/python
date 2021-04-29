import math

# def calc_square(ab, bc, ac):
#     p = (ab + bc + ac) / 2
#     s = math.sqrt(p * (p - ab)* (p - bc) * (p - ac))

#     return s

# square = calc_square(10, 10, 10)
# print(square)

# square = calc_square(-2, 8, 8)
# print(square)


# def calc_square(ab, bc, ac):
#     if ab <= 0 or bc <= 0 or  ac <= 0:
#         raise ValueError("One of the sides is les or equal to 0.")

#     p = (ab + bc + ac) / 2
#     s = math.sqrt(p * (p - ab)* (p - bc) * (p - ac))

#     return s


# square = calc_square(-2, 8, 8)
# print(square)


class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""


def calc_square(ab, bc, ac):
    if ab <= 0 or bc <= 0 or ac <= 0:
        raise InvalidTriangleError("One of the sides is less or equal to 0.")

    p = (ab + bc + ac) / 2
    s = math.sqrt(p * (p - ab) * (p - bc) * (p - ac))

    return s


try:
    square = calc_square(10, 8, 8)
except InvalidTriangleError as ex:
    print(ex)
else:
    print(square)
