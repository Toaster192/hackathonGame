from threading import Timer

import pygame

import src.Colors as Color
import src.Config as Config
import src.util as util
from .Particles import ParticleFieldEmitter
from .Vector import Vector2


class Player:
    def __init__(self, x, y, width, height, color):
        self.pos = Vector2(x, y)
        self.size = Vector2(width, height)
        self.color = color
        self.jumping = True
        self.facing = True
        self.left = False
        self.right = False
        self.jumpspeed = Config.PLAYER_JUMP_SPEED
        self.can_double_jump = False
        self.double_jump_cooldown = Config.PLAYER_DEOUBLEJUMP_COOLDOWN
        self.walkCount = 0
        self.v = Vector2(0, 0)
        self.speed = Config.PLAYER_MAX_SPEED
        self.dead = False

        pygame.display.init()
        self.calm_image = util.load_image('img/face_calm.png',
                                          (Config.PLAYER_WIDTH,
                                           Config.PLAYER_WIDTH))
        self.excited_image = util.load_image('img/face_excited.png',
                                             (Config.PLAYER_WIDTH,
                                              Config.PLAYER_WIDTH))
        self.image = self.calm_image

        self.emitter = ParticleFieldEmitter(
            colors=(
                [Color.WHITE, Color.YELLOW, Color.ORANGE, Color.RED,
                 Color.GRAY, Color.DARK_GRAY, Color.darker(Color.DARK_GRAY, 2),
                 Color.BLACK]), pos=Vector2(0, 0),
            size=Vector2(Config.PLAYER_WIDTH, Config.PLAYER_HEIGHT),
            velocity=Vector2(0, -16), velocity_jitter=Vector2(4, 8),
            accel=Vector2(0, -12), gen_delay=0.01, duration=2,
            sizes=[3, 5, 8, 6, 8, 16])

    def moveLeft(self, dt):
        if self.v.x > 0:
            self.stopMoving(dt)
        self.v -= Vector2(Config.PLAYER_ACCELERATION * dt, 0)
        if self.v.x < -self.speed:
            self.v.x = -self.speed

    def moveRight(self, dt):
        if self.v.x < 0:
            self.stopMoving(dt)
        self.v += Vector2(Config.PLAYER_ACCELERATION * dt, 0)
        if self.v.x > self.speed:
            self.v.x = self.speed

    def allow_double_jump(self):
        self.can_double_jump = True

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.v.y = -self.jumpspeed
            self.image = self.excited_image
            Timer(self.double_jump_cooldown, self.allow_double_jump).start()
            # self.allow_double_jump()
        else:
            if self.can_double_jump:
                self.can_double_jump = False
                self.v.y = -self.jumpspeed

    def stopMoving(self, dt):
        self.v.x *= 1 if dt == 0 else 0.01 / dt

    def update(self, dt, keys, blocks):
        surroundings = self.calculate_surroundings(blocks)

        if keys[pygame.K_LEFT]:
            self.moveLeft(dt)
            self.facing = False

        if keys[pygame.K_RIGHT]:
            self.moveRight(dt)
            self.facing = False

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.stopMoving(dt)
            self.facing = True

        left_border = int(max(self.check_collision_left(surroundings),
                              Config.GAMEFIELD_LEFT_BORDER))

        if int(self.pos.x) < left_border - self.v.x * dt:
            self.v.x = 0
            self.pos.x = left_border
        else:
            right_border = int(min(self.check_collision_right(surroundings),
                                   Config.GAMEFIELD_RIGHT_BORDER - 1))
            if (int(self.pos.x) > (
                    right_border - Config.PLAYER_WIDTH) - self.v.x * dt):
                self.v.x = 0
                self.pos.x = (right_border - Config.PLAYER_WIDTH)

        if keys[pygame.K_UP]:
            self.jump()

        self.v += Vector2(0, Config.PLAYER_GRAVITY * dt)
        self.pos += self.v * dt

        bottom_border = int(min(self.check_collision_down(surroundings),
                                Config.GAMEFIELD_BOTTOM_BORDER))

        if int(self.pos.y) > bottom_border - Config.PLAYER_HEIGHT:
            self.v.y = 0
            self.pos.y = (bottom_border - Config.PLAYER_HEIGHT)
            self.jumping = False
            self.image = self.calm_image
        else:
            top_border = int(self.check_collision_up(surroundings))
            if int(self.pos.y) < top_border + self.v.y * dt:
                self.v.y = Config.BLOCK_SPEED[1]
                self.pos.y = top_border + 3
                if self.check_collision_down(surroundings) <= 1:
                    event = pygame.event.Event(Config.PLAYER_DEAD_EVENT)
                    pygame.event.post(event)

        # self.emitter.pos = self.pos
        # self.emitter.update(dt)

    def render(self, surface):
        pygame.draw.rect(surface, self.color,
                         pygame.Rect(self.pos.x, self.pos.y, self.size.x,
                                     self.size.y))
        surface.blit(self.image,
                     pygame.Rect(self.pos.x, self.pos.y,
                                 self.size.x, self.size.x))
        # self.emitter.render(surface)

    def calculate_surroundings(self, blocks):
        around = []
        for block in blocks:
            if self.pos.manhattan_distance(
                    Vector2(block.x,
                            block.y)) < (Config.COLLISION_DISTANCE *
                                         Config.BLOCK_WIDTH):
                around += block.objects
        return around

    def check_collision_right(self, surroundings):
        border = 1e6
        for square in surroundings:
            if (square.bounds.x > self.pos.x + Config.PLAYER_WIDTH / 2 and
                    self.pos.y - Config.BLOCK_HEIGHT < square.bounds.y <
                    self.pos.y + Config.PLAYER_HEIGHT - 4):
                border = min(border, square.bounds.x)
        return border

    def check_collision_left(self, surroundings):
        border = -1e6
        for square in surroundings:
            if (square.bounds.x + Config.BLOCK_WIDTH / 2 < self.pos.x and
                    self.pos.y - Config.BLOCK_HEIGHT < square.bounds.y <
                    self.pos.y + Config.PLAYER_HEIGHT - 4):
                border = max(border, square.bounds.x + Config.BLOCK_WIDTH)
        return border

    def check_collision_down(self, surroundings):
        border = 1e6
        for square in surroundings:
            if (square.bounds.y > self.pos.y + Config.PLAYER_HEIGHT / 2 and
                    self.pos.x - Config.BLOCK_WIDTH < square.bounds.x <
                    self.pos.x + Config.PLAYER_WIDTH):
                border = min(border, square.bounds.y)
        return border

    def check_collision_up(self, surroundings):
        border = -1e6
        for square in surroundings:
            if (square.bounds.y < self.pos.y and
                    self.pos.x - Config.BLOCK_WIDTH < square.bounds.x <
                    self.pos.x + Config.PLAYER_WIDTH):
                border = max(border, square.bounds.y + Config.BLOCK_HEIGHT)
        return border
