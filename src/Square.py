import pygame
from src.GameObject import GameObject
import src.Colors as Colors
import src.Config as Config


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

    def render(self, surface):
        self.paint_tile(surface, self.bounds.x, self.bounds.y, self.bounds.w,
                        self.bounds.height, Colors.CYAN)

    # THE 7.999 JUST WORKS - DON'T ASK ME WHY
    def detects_collision(self, blocks):
        if self.bounds.y + self.bounds.height + 7.999 >= Config.GAMEFIELD_BOTTOM_BORDER - 1:
            return True
        for block in blocks:
            for square in block.objects:
                if self.bounds.y + self.bounds.height + 7.999 >= square.bounds.y - 1 and \
                        self.bounds.x == square.bounds.x:
                    return True
        return False
