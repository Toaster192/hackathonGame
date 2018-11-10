from src.Square import Square
from src.GameObject import GameObject
import pygame
import src.Config as Config


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

    def move(self, dt, blocks, *speed):
        for square in self.objects:
            if square.detects_collision(blocks) and self.falling == True:
                self.falling = False
                for square in self.objects:
                    square.speed = (0, 0)
                    #ONE-LINER - DON'T ASK, DON'T WANT ME TO DO ANYTHING WITH IT AGAIN
                    square.bounds.y = Config.GAMEFIELD_BOTTOM_BORDER - 1 - \
                                      ((Config.GAMEFIELD_BOTTOM_BORDER - (square.bounds.y)) // \
                                       Config.BLOCK_HEIGHT) * Config.BLOCK_HEIGHT
                self.speed = (0, 0)
                event = pygame.event.Event(pygame.USEREVENT, {"ev": "block_falled"})
                pygame.event.post(event)

        for square in self.objects:
            square.update(dt)
