import pygame
import src.Config as Config
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
        self.walkCount = 0
        self.v = Vector2(0, 0)
        self.speed = Config.PLAYER_MAX_SPEED

    def moveLeft(self):
        if self.v.x > 0:
            self.stopMoving()
        self.v -= Vector2(Config.PLAYER_ACCELERATION, 0)
        if self.v.x < -self.speed:
            self.v.x = -self.speed

    def moveRight(self):
        if self.v.x < 0:
            self.stopMoving()
        self.v += Vector2(Config.PLAYER_ACCELERATION, 0)
        if self.v.x > self.speed:
            self.v.x = self.speed

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.v.y = -self.jumpspeed

    def stopMoving(self):
        self.v.x *= 0.6

    def update(self, dt, keys, blocks):
        surroundings = self.calculate_surroundings(blocks)

        if keys[pygame.K_LEFT]:
            self.moveLeft()
            self.facing = False

        if keys[pygame.K_RIGHT]:
            self.moveRight()
            self.facing = False

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.stopMoving()
            self.facing = True

        left_border = int(max(self.check_collision_left(surroundings),
                              Config.GAMEFIELD_LEFT_BORDER))

        if int(self.pos.x) < left_border - self.v.x * dt:
            self.v.x = 0
            self.pos.x = left_border
        else:
            right_border = int(min(self.check_collision_right(surroundings),
                                   Config.GAMEFIELD_RIGHT_BORDER))
            if (int(self.pos.x) > (
                    right_border - Config.PLAYER_WIDTH) - self.v.x * dt):
                self.v.x = 0
                self.pos.x = (right_border - Config.PLAYER_WIDTH)

        if keys[pygame.K_UP]:
            self.jump()

        self.v += Vector2(0, Config.PLAYER_GRAVITY)
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
                self.v.y = 0
                self.pos.y = top_border

    def render(self, surface):
        pygame.draw.rect(surface, self.color,
                         pygame.Rect(self.pos.x, self.pos.y, self.size.x,
                                     self.size.y))

    def calculate_surroundings(self, blocks):
        around = []
        for block in blocks:
            if self.pos.manhattan_distance(
                    Vector2(block.x, block.y)) < Config.COLLISION_DISTANCE * Config.BLOCK_WIDTH:
                around += block.objects
        return around

    def check_collision_right(self, surroundings):
        border = 1e6
        for square in surroundings:
            if square.bounds.x > self.pos.x + Config.PLAYER_WIDTH/2 and self.pos.y - Config.BLOCK_HEIGHT < square.bounds.y < self.pos.y + Config.PLAYER_HEIGHT - 4:
                border = min(border, square.bounds.x)
        return border

    def check_collision_left(self, surroundings):
        border = -1e6
        for square in surroundings:
            if square.bounds.x + Config.BLOCK_WIDTH/2 < self.pos.x and self.pos.y - Config.BLOCK_HEIGHT < square.bounds.y < self.pos.y + Config.PLAYER_HEIGHT - 4:
                border = max(border, square.bounds.x + Config.BLOCK_WIDTH)
        return border

    def check_collision_down(self, surroundings):
        border = 1e6
        for square in surroundings:
            if square.bounds.y > self.pos.y + Config.PLAYER_HEIGHT/2 and self.pos.x - Config.BLOCK_WIDTH < square.bounds.x < self.pos.x + Config.PLAYER_WIDTH:
                border = min(border, square.bounds.y)
        return border

    def check_collision_up(self, surroundings):
        border = -1e6
        for square in surroundings:
            if square.bounds.y < self.pos.y and self.pos.x - Config.BLOCK_WIDTH < square.bounds.x < self.pos.x + Config.PLAYER_WIDTH:
                border = max(border, square.bounds.y + Config.BLOCK_HEIGHT)
        return border
