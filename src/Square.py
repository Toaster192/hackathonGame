import pygame
import src.Config as Config
from src.GameObject import GameObject
#from src.PlaceholderGame import PlaceholderGame.get_grounded_squares as grounded_squares
from src.TilePainter import paint_tile
import src.Colors as Colors
import src.Config as Config


class Square(GameObject):
    def __init__(self, x, y, color, speed, w=Config.BLOCK_WIDTH, h=Config.BLOCK_HEIGHT):
        super().__init__(x, y, w, h, speed)
        self.color = color

    def draw(self, surface):
        paint_tile(surface, self.bounds.x, self.bounds.y, self.bounds.w,
                   self.bounds.height, self.color)
    #THE 7.999 JUST WORKS - DON'T ASK ME WHY
    def detects_collision(self, blocks):
        if self.bounds.y + self.bounds.height + 7.999 >= Config.GAMEFIELD_BOTTOM_BORDER - 1:
            return True
        for block in blocks:
            for square in block.objects:
                if self.bounds.y + self.bounds.height + 7.999 >= square.bounds.y - 1 and \
                        self.bounds.x == square.bounds.x:
                    return True
        return False
