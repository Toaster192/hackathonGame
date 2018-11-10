import src.Config as Config


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.jumping = False
        self.facing = True
        self.left = False
        self.right = False
        self.jumpspeed = -10
        self.walkCount = 0
        self.v_x = 0
        self.v_y = 0
        self.speed = Config.PLAYER_MAX_SPEED

    def moveLeft(self):
        if self.v_x <= (-self.speed + 1):
            self.v_x = -self.speed
        else:
            self.v_x -= 1

    def moveRight(self):
        if self.v_x >= (self.speed - 1):
            self.v_x = self.speed
        else:
            self.v_x += 1

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.v_y = -10

    def stopMoving(self):
        self.v_x += -self.v_x/2
