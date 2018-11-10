from src.Square import Square
from src.GameObject import GameObject


class Block(GameObject):
    def __init__(self, x, y, width, height, array, speed, falling, state, color):
        super(Block, self).__init__(x, y, width, height, speed)
        self.x = x
        self.y = y
        self.bounds.width = width
        self.bounds.height = height
        self.array = array
        self.speed = speed
        self.state = state
        self.color = color
        self.falling = falling
        self.objects = list(map(lambda t: createBlock(t[0], t[1]), array))

    def createBlock(self, x, y):
        return Square(self.x + x, self.y + y, self.color, self.speed)

    def draw(self, surface):
        for square in self.objects:
            square.draw(surface)

    def move(self, dt, *speed):
        for square in self.objects:
            if not square.detects_collision():
                square.update(dt)
            elif square.detects_collision() and self.falling == True:
                self.falling = False
                self.speed = self.speed / 2
                square.update(dt)
            elif square.detects_collision() and self.falling == False:
                square.update(dt)
