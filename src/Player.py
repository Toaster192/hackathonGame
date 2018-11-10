import pygame
import src.Config as Config
from .Vector import Vector2


class Player:
    def __init__(self, x, y, width, height, color):
        self.pos = Vector2(x, y)
        self.size = Vector2(width, height)
        self.color = color
        self.jumping = False
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

    def update(self, dt, keys):
        if keys[pygame.K_LEFT]:
            self.moveLeft()
            self.facing = False

        if keys[pygame.K_RIGHT]:
            self.moveRight()
            self.facing = False

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.stopMoving()
            self.facing = True

        if (int(self.pos.x) <
                int(Config.GAMEFIELD_LEFT_BORDER) - self.v.x * dt):
            self.v.x = 0
            self.pos.x = Config.GAMEFIELD_LEFT_BORDER
        elif (int(self.pos.x) >
              ((int(Config.GAMEFIELD_RIGHT_BORDER)) -
               Config.PLAYER_WIDTH) - self.v.x * dt):
            self.v.x = 0
            self.pos.x = (Config.GAMEFIELD_RIGHT_BORDER -
                          Config.PLAYER_WIDTH-1)

        if pygame.event.poll().type == pygame.USEREVENT:
            self.block = BlockGenerator.generate((0, 50))

        if not self.jumping:
            if keys[pygame.K_UP]:
                self.jump()

        self.v += Vector2(0, Config.PLAYER_GRAVITY)
        self.pos += self.v * dt

        if (int(self.pos.y) > int(
                Config.GAMEFIELD_BOTTOM_BORDER - Config.PLAYER_HEIGHT)):
            self.v.y = 0
            self.pos.y = (Config.GAMEFIELD_BOTTOM_BORDER -
                          Config.PLAYER_HEIGHT)
            self.jumping = False

    def render(self, surface):
        pygame.draw.rect(surface, self.color,
                         pygame.Rect(self.pos.x, self.pos.y, self.size.x,
                                     self.size.y))
