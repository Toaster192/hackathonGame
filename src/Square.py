import pygame

import src.Colors as Colors
import src.Config as Config
from src.GameObject import GameObject


class Square(GameObject):
    def __init__(self, x, y, color, speed, w=Config.BLOCK_WIDTH,
                 h=Config.BLOCK_HEIGHT):
        super().__init__(x, y, w, h, speed)
        self.color = color

    def paint_tile(self, surface, x, y, w, h, color, border=0.125):
        pygame.draw.rect(surface, color, pygame.Rect(x, y, w, h))
        pygame.draw.polygon(surface, Colors.brighter(color), [
            (x, y),
            (x + w, y),
            (x + w * (1 - border), y + h * border),
            (x + w * border, y + h * border),
            (x + w * border, y + h * (1 - border)),
            (x, y + h)
        ])
        pygame.draw.polygon(surface, Colors.darker(color), [
            (x + w, y + h),
            (x, y + h),
            (x + w * border, y + h * (1 - border)),
            (x + w * (1 - border), y + h * (1 - border)),
            (x + w * (1 - border), y + h * border),
            (x + w, y)
        ])

    def render(self, surface, offset):
        self.paint_tile(surface, self.bounds.x + offset.x, self.bounds.y + offset.y, self.bounds.w,
                        self.bounds.height, self.color)

    def detects_collision(self, blocks):
        if (self.bounds.y + self.bounds.height + Config.BLOCK_HEIGHT / 2 >=
                Config.GAMEFIELD_BOTTOM_BORDER - 1):
            return True
        for block in blocks:
            for square in block.objects:
                if (square.bounds.y - 1 <= self.bounds.y + self.bounds.height +
                        Config.BLOCK_HEIGHT / 2 <= square.bounds.y +
                        Config.BLOCK_HEIGHT // 4 and
                        self.bounds.x == square.bounds.x):
                    return True
        return False
