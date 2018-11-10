from pygame.rect import Rect

class Bounds:
    def __init__(self, x, y, w, h):
        self.x = float(x)
        self.y = float(y)
        self.h = float(h)
        self.w = float(w)
        self.left = float(x)
        self.right = float(x + w)
        self.top = float(y)
        self.bottom = float(y + h)
        self.width = self.w
        self.height = self.h
        self.centerx = self.x + self.width / 2
        self.centery = self.y + self.height / 2
        self.center = (self.centerx, self.centery)


class GameObject:
    def __init__(self, x, y, w, h, speed=(0, 0)):
        self.bounds = Bounds(x, y, w, h)
        self.speed = speed
        # print(self.bounds.x)
        #self.bounds = Rect(float(x),float(y),float(w),float(h))

    @property
    def left(self):
        return self.bounds.left

    @property
    def right(self):
        return self.bounds.right

    @property
    def top(self):
        return self.bounds.top

    @property
    def bottom(self):
        return self.bounds.bottom

    @property
    def width(self):
        return self.bounds.width

    @property
    def height(self):
        return self.bounds.height

    @property
    def center(self):
        return self.bounds.center

    @property
    def centerx(self):
        return self.bounds.centerx

    @property
    def centery(self):
        return self.bounds.centery

    def draw(self, surface):
        pass

    def move(self, dt, dx, dy):
        self.bounds.x = self.bounds.x + dx * dt
        self.bounds.y = self.bounds.y + dy * dt

    def update(self, dt):
        if self.speed == [0, 0]:
            return

        self.move(dt, *self.speed)

    def __del__(self):
        pass
