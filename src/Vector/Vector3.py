import numbers

from . import Vector2


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def tuple(self):
        return self.x, self.y, self.z

    def floor(self):
        return Vector3(int(self.x), int(self.y), int(self.z))

    def __add__(self, other):
        if not isinstance(other, Vector3):
            raise ArithmeticError
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector3):
            raise ArithmeticError
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, numbers.Number):
            raise ArithmeticError
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        if not isinstance(other, numbers.Number) or other == 0:
            raise ArithmeticError
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other):
        if not isinstance(other, numbers.Number) or other == 0:
            raise ArithmeticError
        return Vector3(self.x // other, self.y // other, self.z // other)

    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def distance(self, other):
        if not isinstance(other, Vector2):
            raise ArithmeticError
        return (self - other).length()

    def manhattan_distance(self, other):
        if not isinstance(other, Vector2):
            raise ArithmeticError
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(
            self.z - other.z)

    # Vector swizzling
    def __getattr__(self, key):
        if match('^[xyz]{2}$', key):
            v = []
            for c in key:
                v.append(getattr(self, c))
            return Vector2(*v)
        elif match('^[xyz]{3}$', key):
            v = []
            for c in key:
                v.append(getattr(self, c))
            return Vector3(*v)
