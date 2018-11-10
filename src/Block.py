from src.Square import Square
from src.GameObject import GameObject
import pygame


class Block(GameObject):
    def __init__(self, x, y, width, height, array, speed, falling, color):
        super(Block, self).__init__(x, y, width, height, speed)
        self.x = x
        self.y = y
        self.bounds.width = width
        self.bounds.height = height
        self.array = array
        self.speed = speed
        self.color = color
        self.falling = falling
        self.objects = list(map(lambda t: self.createBlock(t[0], t[1]), array))

    def createBlock(self, x, y):
        return Square(self.x + x, self.y + y, self.color, self.speed)

    def draw(self, surface):
        for square in self.objects:
            square.draw(surface)

    def move(self, dt, *speed):
        for square in self.objects:
            if not square.detects_collision("horizontal","left"):
                square.update(dt)
            elif square.detects_collision("horizontal","left") and self.falling == True:
                self.falling = False
                for square in self.objects:
                    square.speed = (0, 0)
                self.speed = (0, 0)
                square.update(dt)
                print(speed)
                event = pygame.event.Event(pygame.USEREVENT, {"ev": "block_falled"})
                pygame.event.post(event)
            elif square.detects_collision("horizontal","left") and self.falling == False:
                square.update(dt)
