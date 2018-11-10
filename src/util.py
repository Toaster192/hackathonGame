import pygame


def clamp(x, mn, mx):
    return min(max(x, mn), mx)


def interpolate(array, x):
    x = clamp(x, 0, 1)

    if x == 0 or len(array) == 1:
        return array[0]
    if x == 1:
        return array[-1]
    x *= len(array) - 1
    int_part = int(x)
    frac_part = x - int_part
    return array[int_part] * (1 - frac_part) + array[int_part + 1] * frac_part


def interpolate_tuple(array, x):
    return tuple(map(lambda t: interpolate(t, x), zip(*array)))


def load_image(path, size):
    image = pygame.image.load(path)
    image.convert()
    image = pygame.transform.scale(image, size)
    return image
