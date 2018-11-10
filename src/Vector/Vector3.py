import numbers


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
