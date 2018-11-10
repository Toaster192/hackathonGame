import pygame
import src.Config as Config
from src.GameObject import GameObject
#from src.PlaceholderGame import PlaceholderGame.get_grounded_squares as grounded_squares
from src.TilePainter import paint_tile
import src.Colors as Colors



class Square(GameObject):
    def __init__(self, x, y, color, speed, w=32, h=32):
        super().__init__(x, y, w, h, speed)
        self.color = color

    def draw(self, surface):
        paint_tile(surface, self.bounds.x, self.bounds.y, self.bounds.w, self.bounds.height, Colors.CYAN)

    def detects_collision(self, mode, direction=""):
        if(mode == "vertical"):
            #top_squares = grounded_squares.get_top_squares
            #return top_squares[i].y <= self.bottom + 1 || self.bottom == 1
            return False
        elif(mode == "horizontal"):
            grounded_squares = [[(i*Config.BLOCK_WIDTH,j*Config.BLOCK_WIDTH) for i in range(16)] for j in range(16)]
            print(grounded_squares)
            #if(dir == "left"):
            #    x = self.left//Config.BLOCK_WIDTH
            #elif(dir == "right"):
            #    x = self.left//Config.BLOCK_WIDTH + Config.BLOCK_WIDTH
            #return grounded_squares[x][self.top//Config.BLOCK_HEIGHT] || grounded_squares[x][self.top//Config.BLOCK_HEIGHT]
            return False
        return False
