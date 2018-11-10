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
                   self.bounds.height, Colors.CYAN)

    def detects_collision(self, mode, direction=""):
        if self.bounds.y + self.bounds.height >= Config.GAMEFIELD_BOTTOM_BORDER - 1:
            return True
        return False