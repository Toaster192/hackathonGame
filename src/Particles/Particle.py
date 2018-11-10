import pygame
from time import time
from src.util import interpolate
from src.Vector import Vector3


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

        self.velocity += self.accel * dt
        self.pos += self.velocity * dt

    def render(self, surface):
        if self.start_time + self.duration < time():
            return

        life = (time() - self.start_time) / self.duration
        size = interpolate(self.sizes, life)
        color = interpolate(list(map(lambda t: Vector3(*t), self.colors)),
                            life)

        pygame.draw.circle(surface, color.floor().tuple(),
                           self.pos.floor().tuple(), int(size))
