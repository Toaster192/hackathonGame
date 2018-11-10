WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
DARK_GRAY = (63, 63, 63)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

ORANGE = (255, 165, 0)

colors = (RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE)


def darker(color, magnitude=1.25):
    return tuple(int(c/magnitude) for c in color)


def brighter(color, magnitude=1.25):
    return tuple(int(255 - (255 - c)/magnitude) for c in color)
