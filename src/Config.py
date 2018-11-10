import pygame

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 640
BLOCK_WIDTH = 16
BLOCK_HEIGHT = 16
BLOCK_COUNT = 16
BLOCK_SPEED = (0, 200)
GAMEFIELD_WIDTH = BLOCK_WIDTH * BLOCK_COUNT + 4
GAMEFIELD_LEFT_BORDER = SCREEN_WIDTH / 2 - GAMEFIELD_WIDTH / 2 + 1
GAMEFIELD_RIGHT_BORDER = GAMEFIELD_LEFT_BORDER + GAMEFIELD_WIDTH - 2
GAMEFIELD_TOP_BORDER = 0 + 1
GAMEFIELD_BOTTOM_BORDER = SCREEN_HEIGHT - 1
PLAYER_MAX_SPEED = 250
PLAYER_ACCELERATION = 900
PLAYER_GRAVITY = 1200
PLAYER_JUMP_SPEED = 400
PLAYER_DEOUBLEJUMP_COOLDOWN = 0.3
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 32
GAMEFIELD_WIDTH = BLOCK_WIDTH * BLOCK_COUNT
GAMEFIELD_HEIGHT = SCREEN_HEIGHT
COLLISION_DISTANCE = 6  # block widths from player origin

BLOCK_FELL_EVENT = pygame.USEREVENT + 1
PLAYER_DEAD_EVENT = pygame.USEREVENT + 2
BLOCKS_FALLING = 10

GRAPHICS_SCREENSHAKE_MAGNITUDE = 3
GRAPHICS_SCREENSHAKE_DAMPENING = 0.1
GRAPHICS_HEIGHT_SMOOTHING = 0.9