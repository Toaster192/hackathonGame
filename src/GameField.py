import pygame
import src.Config as Config


class GameField:
    def __init__(self):
        self.width = Config.GAMEFIELD_WIDTH
        self.height = Config.GAMEFIELD_HEIGHT
        self.x = Config.SCREEN_WIDTH / 2 - self.width / 2
        self.y = 0

    def render(self, surface):
        pygame.draw.rect(surface, pygame.Color('white'), pygame.Rect(
            self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, pygame.Color('black'), pygame.Rect(
            self.x + 1, self.y + 1, self.width - 2, self.height - 2))

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
