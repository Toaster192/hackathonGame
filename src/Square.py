import pygame

from src.GameObject import GameObject
from src.TilePainter import paint_tile
import src.Colors as Colors


class Square(GameObject):
    def __init__(self, x, y, color, speed, w=32, h=32):
        GameObject.__init__(self, x, y, w, h, speed)
        self.color = color

    def draw(self, surface):
        paint_tile(surface, self.bounds.x, self.bounds.y, self.bounds.w, self.bounds.height, Colors.CYAN)
