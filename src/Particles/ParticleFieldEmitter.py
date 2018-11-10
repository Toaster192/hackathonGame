from time import time
from random import uniform
from .Particle import Particle


class ParticleFieldEmitter:
    def __init__(self, color_begin, color_end, color_jitter, pos, size,
                 velocity, velocity_jitter, accel, gen_delay, duration,
                 size_begin, size_end):
        self.color_begin = color_begin
        self.color_end = color_end
        self.color_jitter = color_jitter
        self.pos = pos
        self.size = size
        self.velocity = velocity
        self.velocity_jitter = velocity_jitter
        self.accel = accel
        self.gen_delay = gen_delay
        self.duration = duration
        self.size_begin = size_begin
        self.size_end = size_end
        self.particles = []
        self.next_particle_time = time()

    def __del__(self):
        self.particles.clear()

    def update(self, dt):
        while self.next_particle_time < time():
            random_pos = tuple(
                p + uniform(0, s) for p, s in zip(self.pos, self.size))
            random_vel = tuple(v + uniform(-j, j) for v, j in
                               zip(self.velocity, self.velocity_jitter))
            c_jitter = uniform(0, self.color_jitter)
            random_color = tuple(b * (1 - c_jitter) + e * c_jitter for b, e in
                                 zip(self.color_begin, self.color_end))

            self.particles.append(
                Particle(random_color, self.color_end, random_pos, random_vel,
                         self.accel, self.duration, self.size_begin,
                         self.size_end))
            self.next_particle_time += self.gen_delay

        # Delete old particles
        self.particles = [x for x in self.particles if
                          time() < x.start_time + self.duration]
        for particle in self.particles:
            particle.update(dt)

    def render(self, surface):
        for particle in self.particles:
            particle.render(surface)
