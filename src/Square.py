import pygame
import src.Config as Config
from src.GameObject import GameObject
from src.PlaceholderGame import PlaceholderGame.get_grounded_squares as grounded_squares
 
 
class Square(GameObject):
    def __init__(self, x, y, color, w=32, h=32):
        super().__init__(x, y, w, h)
        #GameObject.__init__(self, x, y, w, h)
        self.color = color
 
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def detects_collision(self, mode, direction=""):
        if(mode == "vertical"):
            top_squares = grounded_squares.get_top_squares
            return top_squares[i].y <= self.bottom + 1 || self.bottom == 1
        elif(mode == "horizontal"):
            if(dir == "left"):
                x = self.left//Config.BLOCK_WIDTH
            elif(dir == "right"):
                x = self.left//Config.BLOCK_WIDTH + Config.BLOCK_WIDTH
            return grounded_squares[x][self.top//Config.BLOCK_HEIGHT] || grounded_squares[x][self.top//Config.BLOCK_HEIGHT]
        return False
