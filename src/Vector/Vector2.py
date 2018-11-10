import numbers
from re import match

from . import Vector3


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tuple(self):
        return self.x, self.y

    def floor(self):
        return Vector2(int(self.x), int(self.y))

    def __add__(self, other):
        if not isinstance(other, Vector2):
            raise ArithmeticError
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2):
            raise ArithmeticError
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, numbers.Number):
            raise ArithmeticError
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if not isinstance(other, numbers.Number) or other == 0:
            raise ArithmeticError
        return Vector2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        if not isinstance(other, numbers.Number) or other == 0:
            raise ArithmeticError
        return Vector2(self.x // other, self.y // other)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance(self, other):
        if not isinstance(other, Vector2):
            raise ArithmeticError
        return (self - other).length()

    def manhattan_distance(self, other):
        if not isinstance(other, Vector2):
            raise ArithmeticError
        return abs(self.x - other.x) + abs(self.y - other.y)

    # Swizzling
    def __getattr__(self, key):
        if match('^[xy]{2}$', key):
            v = []
            for c in key:
                v.append(getattr(self, c))
            return Vector2(*v)
        elif match('^[xy]{3}$', key):
            v = []
            for c in key:
                v.append(getattr(self, c))
            return Vector3(*v)
