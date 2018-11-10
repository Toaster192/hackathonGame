from random import uniform
from time import time

from src.Vector import Vector2
from .Particle import Particle


class ParticleFieldEmitter:
    def __init__(self, colors, pos, size, velocity, velocity_jitter, accel,
                 gen_delay, duration, sizes):
        self.colors = colors
        self.pos = pos
        self.size = size
        self.velocity = velocity
        self.velocity_jitter = velocity_jitter
        self.accel = accel
        self.gen_delay = gen_delay
        self.duration = duration
        self.sizes = sizes
        self.particles = []
        self.next_particle_time = time()

    def __del__(self):
        self.particles.clear()

    def update(self, dt, spawn_particles=True):
        while self.next_particle_time < time() and spawn_particles:
            random_pos = self.pos + Vector2(uniform(0, self.size.x),
                                            uniform(0, self.size.y))
            j = self.velocity_jitter
            random_vel = self.velocity + Vector2(uniform(-j.x, j.x),
                                                 uniform(-j.y, j.y))

            self.particles.append(
                Particle(self.colors, random_pos, random_vel, self.accel,
                         self.duration, self.sizes))
            self.next_particle_time += self.gen_delay

        # Delete old particles
        self.particles = [x for x in self.particles if
                          time() < x.start_time + self.duration]
        for particle in self.particles:
            particle.update(dt)

    def render(self, surface, offset):
        for particle in self.particles:
            particle.render(surface, offset)
