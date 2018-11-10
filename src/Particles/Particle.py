import pygame
from time import time


class Particle:
    def __init__(self, color_begin, color_end, pos, velocity, accel, duration,
                 size_begin, size_end):
        self.color_begin = color_begin
        self.color_end = color_end
        self.pos = pos
        self.velocity = velocity
        self.accel = accel
        self.duration = duration
        self.size_begin = size_begin
        self.size_end = size_end
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
        size = int((1 - life) * self.size_begin + life * self.size_end)
        color = tuple(
            int((1 - life) * b + life * e) for b, e in
            zip(self.color_begin, self.color_end))

        pygame.draw.circle(surface, color, tuple(map(int, self.pos)), size)
