import pygame

import src.Colors as Color
import src.Config as Config
from src.GameObject import GameObject
from src.Particles import ParticleFieldEmitOnce
from src.Square import Square
from src.Vector import Vector2


class Block(GameObject):
    def __init__(self, x, y, width, height, array, speed, falling, color):
        super(Block, self).__init__(x, y, width, height, speed)
        self.x = x
        self.y = y
        self.bounds.width = width
        self.bounds.height = height
        self.array = array
        self.speed = speed
        self.color = color
        self.falling = falling
        self.generatedNew = False
        self.objects = list(map(lambda t: self.createBlock(t[0], t[1]), array))

    def createBlock(self, x, y):
        return Square(self.x + x, self.y + y, self.color, self.speed)

    def render(self, surface):
        for square in self.objects:
            square.render(surface)

    def move(self, dt, blocks, genHeight, *speed):
        for square in self.objects:
            if square.detects_collision(blocks) and self.falling:
                self.falling = False
                for ssquare in self.objects:
                    ssquare.speed = (0, 0)
                    # ONE-LINER - DON'T ASK,
                    # DON'T WANT ME TO DO ANYTHING WITH IT AGAIN
                    ssquare.bounds.y = (Config.GAMEFIELD_BOTTOM_BORDER - 1 -
                                        ((Config.GAMEFIELD_BOTTOM_BORDER -
                                         (ssquare.bounds.y)) //
                                         Config.BLOCK_HEIGHT) *
                                        Config.BLOCK_HEIGHT)
                self.speed = (0, 0)
                ParticleFieldEmitOnce(colors=[Color.WHITE, Color.GRAY],
                                      pos=Vector2(square.bounds.x,
                                                  square.bounds.y +
                                                  square.bounds.h),
                                      size=Vector2(square.bounds.w, 0),
                                      velocity=Vector2(0, -20),
                                      velocity_jitter=Vector2(20, 10),
                                      accel=Vector2(0, 30), gen_delay=0.001,
                                      duration=1, sizes=[2, 0],
                                      emitter_duration=0.1)

        for square in self.objects:
            square.update(dt)

        if self.speed != (0, 0):
            self.x += self.speed[0] * dt
            self.y += self.speed[1] * dt

        if (not self.generatedNew and (self.y >= genHeight or
                                       not self.falling)):
            event = pygame.event.Event(Config.BLOCK_FELL_EVENT)
            pygame.event.post(event)
            self.generatedNew = True
