import numbers


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