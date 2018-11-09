import pygame
 
from src.GameObject import GameObject
 
 
class Square(GameObject):
    def __init__(self, x, y, color, w=32, h=32):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
 
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)