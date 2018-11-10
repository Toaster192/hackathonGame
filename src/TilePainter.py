import pygame
from src.Colors import brighter, darker


def paint_tile(surface, x, y, w, h, color, border=0.125):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, w, h))
    pygame.draw.polygon(surface, brighter(color), [
        (x, y),
        (x + w, y),
        (x + w*(1-border), y + h*border),
        (x + w*border, y + h*border),
        (x + w*border, y + h*(1-border)),
        (x, y + h)
    ])
    pygame.draw.polygon(surface, darker(color), [
        (x + w, y + h),
        (x, y + h),
        (x + w*border, y + h*(1-border)),
        (x + w*(1-border), y + h*(1-border)),
        (x + w*(1-border), y + h*border),
        (x + w, y)
    ])
