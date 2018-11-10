from src.Square import Square
from src.GameObject import GameObject


class Block(GameObject):
    def __init__(self, x, y, width, height, array, speed, state, color):
        super(Block, self).__init__(x, y, width, height, speed)
        self.x = x
        self.y = y
        self.bounds.width = width
        self.bounds.height = height
        self.speed = speed
        self.array = array
        self.state = state
        self.color = color
        self.objects = list(map(lambda t: self.createBlock(t[0], t[1]), array))


    def createBlock(self, x, y):
        return Square(self.x + x, self.y + y, self.color, self.speed)

    def draw(self, surface):
        for square in self.objects:
            square.draw(surface)

    def move(self, dt, dx = 1, dy = 0):
        self.y = self.y + self.speed[0] * dt
        for square in self.objects:
            square.update(dt)
