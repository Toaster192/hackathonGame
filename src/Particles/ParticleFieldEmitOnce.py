from time import time

from .ParticleFieldEmitter import ParticleFieldEmitter


class ParticleFieldEmitOnce(ParticleFieldEmitter):
    def __init__(self, colors, pos, size, velocity, velocity_jitter, accel,
                 gen_delay, duration, sizes, emitter_duration):
        super().__init__(colors, pos, size, velocity, velocity_jitter, accel,
                         gen_delay, duration, sizes)
        self.spawn_time = time()
        self.emitter_duration = emitter_duration
        # Cyclic imports are a pain in the ass
        __import__('src').add_particles(self)
        self.remove_particles = __import__('src').remove_particles

    def update(self, dt):
        if time() > self.spawn_time + self.emitter_duration + self.duration:
            self.remove_particles(self)
            return
        super().update(dt, spawn_particles=(time() < self.spawn_time + self.emitter_duration))

    def render(self, surface):
        super().render(surface)
