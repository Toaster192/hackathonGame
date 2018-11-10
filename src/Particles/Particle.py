import pygame
from time import time
from src.util import interpolate, interpolate_tuple


class Particle:
    def __init__(self, colors, pos, velocity, accel, duration, sizes):
        self.colors = colors
        self.pos = pos
        self.velocity = velocity
        self.accel = accel
        self.duration = duration
        self.sizes = sizes
        self.start_time = time()

    def update(self, dt):
        if self.start_time + self.duration < time():
            return

        self.velocity = tuple(
            v + a * dt for v, a in zip(self.velocity, self.accel))
        self.pos = tuple(p + v * dt for p, v in zip(self.pos, self.velocity))

    def render(self, surface):
        if self.start_time + self.duration < time():
            return

        life = (time() - self.start_time) / self.duration
        size = interpolate(self.sizes, life)
        color = interpolate_tuple(self.colors, life)

        pygame.draw.circle(surface, color, tuple(map(int, self.pos)), int(size))
