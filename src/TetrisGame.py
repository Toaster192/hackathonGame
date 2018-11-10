import pygame

import src.Colors as Color
import src.Config as Config
from src.BlockGenerator import BlockGenerator
from src.Game import Game
from src.GameField import GameField
from src.Player import Player


class TetrisGame(Game):
    particle_hooks = []

    def __init__(self):
        super().__init__()
        self.game_field = GameField()
        self.fps_font = None
        self.fps = 0
        self.block_speed = Config.BLOCK_SPEED
        self.generator = BlockGenerator()
        self.player1 = None
        self.blocks = []

    # Gets called at the start of the game
    def init(self, window_name, size):
        super().init(window_name, size)

        self.blocks.append(self.generator.generate(self.block_speed))

        self.player1 = Player(Config.GAMEFIELD_LEFT_BORDER +
                              (Config.GAMEFIELD_WIDTH // 2),
                              Config.GAMEFIELD_BOTTOM_BORDER -
                              Config.PLAYER_HEIGHT, Config.PLAYER_WIDTH,
                              Config.PLAYER_HEIGHT, Color.RED)
        self.fps_font = pygame.font.Font('FreeMono.ttf', 16)
        self.wasted_font = pygame.font.Font('FreeMono.ttf', 46)
        self.wasted_surface = \
                self.wasted_font.render('YOU DEAD!', True, Color.RED)

    # Gets called at game end (pressed [X])
    def clean_up(self):
        pass

    # Gets called on PyGame event
    def handle_event(self, event):
        # print(event)
        if event.type == Config.BLOCK_FELL_EVENT:
            self.blocks.append(self.generator.generate(self.block_speed))
        elif event.type == Config.PLAYER_DEAD_EVENT:
            self.player1.dead = True

    # Called every frame, dt is time between frames
    def loop(self, dt):
        self.fps = 0 if dt == 0 else int(1 / dt)

        keys = pygame.key.get_pressed()
        self.player1.update(dt, keys, self.blocks)

        for i, block in enumerate(self.blocks):
            if block.falling:
                block.move(dt, self.blocks[:i] + self.blocks[i+1:],
                           Config.SCREEN_HEIGHT // Config.BLOCKS_FALLING)

        for particle in self.particle_hooks:
            particle.update(dt)

    # Called after loop(), renders the game screen
    def render(self):
        self.surface.fill(Color.BLACK)

        self.game_field.render(self.surface)

        for block in self.blocks:
            block.render(self.surface)

        self.player1.render(self.surface)

        for particle in self.particle_hooks:
            particle.render(self.surface)

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        if self.player1.dead:
            self.surface.blit(self.wasted_surface, (0, 50))

        pygame.display.update()


def add_particles(particles):
    TetrisGame.particle_hooks.append(particles)


def remove_particles(particles):
    TetrisGame.particle_hooks.remove(particles)
