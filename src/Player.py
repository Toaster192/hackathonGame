from threading import Timer

import pygame

import src.Colors as Color
import src.Config as Config
from src.StaticStore import StaticStore
from .Particles import ParticleFieldEmitter
from .Vector import Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, sprite_l, sprite_r):
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
        self.walking_l = []
        self.walking_r = []
        self.animationArray_r = []
        self.animationArray_l = []
        self.v = Vector2(0, 0)
        self.speed = Config.PLAYER_MAX_SPEED
        self.dead = False

        sprite_sheet_l = pygame.image.load(sprite_l).convert_alpha()
        sprite_sheet_r = pygame.image.load(sprite_r).convert_alpha()
        pygame.sprite.Sprite.__init__(self)

        f1 = sprite_sheet_r.subsurface(0, 0, 15, 31)
        self.animationArray_r.append(f1)
        f2 = sprite_sheet_r.subsurface(16, 0, 15, 31)
        self.animationArray_r.append(f2)
        f3 = sprite_sheet_r.subsurface(32, 0, 15, 31)
        self.animationArray_r.append(f3)
        f4 = sprite_sheet_r.subsurface(48, 0, 15, 31)
        self.animationArray_r.append(f4)
        f5 = sprite_sheet_r.subsurface(64, 0, 15, 31)
        self.animationArray_r.append(f5)
        f6 = sprite_sheet_r.subsurface(80, 0, 15, 31)
        self.animationArray_r.append(f6)
        f7 = sprite_sheet_r.subsurface(96, 0, 15, 31)
        self.animationArray_r.append(f7)

        fl1 = sprite_sheet_l.subsurface(96, 0, 15, 31)
        self.animationArray_l.append(fl1)
        fl2 = sprite_sheet_l.subsurface(80, 0, 15, 31)
        self.animationArray_l.append(fl2)
        fl3 = sprite_sheet_l.subsurface(64, 0, 15, 31)
        self.animationArray_l.append(fl3)
        fl4 = sprite_sheet_l.subsurface(48, 0, 15, 31)
        self.animationArray_l.append(fl4)
        fl5 = sprite_sheet_l.subsurface(32, 0, 15, 31)
        self.animationArray_l.append(fl5)
        fl6 = sprite_sheet_l.subsurface(16, 0, 15, 31)
        self.animationArray_l.append(fl6)
        fl7 = sprite_sheet_l.subsurface(0, 0, 15, 31)
        self.animationArray_l.append(fl7)
        self.render_p = self.animationArray_r[5]
        pygame.display.init()

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
            Timer(self.double_jump_cooldown, self.allow_double_jump).start()
            # self.allow_double_jump()
        else:
            if self.can_double_jump:
                self.can_double_jump = False
                self.v.y = -self.jumpspeed

    def stopMoving(self, dt):
        self.v.x *= 1 if dt == 0 else 0.01 / dt

    def update(self, dt, keys, blocks):
        if self.pos.y + StaticStore.offset.y > Config.SCREEN_HEIGHT + Config.PLAYER_HEIGHT:
            event = pygame.event.Event(Config.PLAYER_DEAD_EVENT)
            pygame.event.post(event)

        surroundings = self.calculate_surroundings(blocks)
        if not self.dead:
            if keys[pygame.K_LEFT]:
                if self.left:
                    self.walkCount += 1
                if self.right:
                    self.walkCount = 0
                self.left = True
                self.right = False
                self.moveLeft(dt)
                self.facing = False
                # if self.jumping:
                #    self.render_p = self.animationArray_l[0]
                # else:
                self.render_p = self.animationArray_l[(
                    (((self.walkCount // 12) % 4) + 1))]

            if keys[pygame.K_RIGHT]:
                if self.right:
                    self.walkCount += 1
                if self.left:
                    self.walkCount = 0
                self.right = True
                self.left = False
                self.moveRight(dt)
                self.facing = False
                # if self.jumping:
                #    self.render_p = self.animationArray_r[0]
                # else:
                self.render_p = self.animationArray_r[(
                    (((self.walkCount // 12) % 4) + 1))]
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.stopMoving(dt)
                self.facing = True
                if self.left:
                    # if self.jumping:
                    #    self.render_p = self.animationArray_l[0]
                    # else:
                    self.render_p = self.animationArray_l[5]
                else:
                    # if self.jumping:
                    #    self.render_p = self.animationArray_r[0]
                    # else:
                    self.render_p = self.animationArray_r[5]
        else:
            self.render_p = self.animationArray_r[0]

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

        if not self.dead:
            if keys[pygame.K_UP]:
                self.jump()
        else:
            self.render_p = self.animationArray_r[0]

        self.v += Vector2(0, Config.PLAYER_GRAVITY * dt)
        self.pos += self.v * dt

        bottom_border = int(min(self.check_collision_down(surroundings),
                                Config.GAMEFIELD_BOTTOM_BORDER))

        if int(self.pos.y) > bottom_border - Config.PLAYER_HEIGHT:
            self.v.y = 0
            self.pos.y = (bottom_border - Config.PLAYER_HEIGHT)
            self.jumping = False
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

    def render(self, surface, offset):
        surface.blit(self.render_p, (self.pos + offset).to_rect(self.size))
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
