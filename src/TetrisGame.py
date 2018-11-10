import pygame

import src.Colors as Color
import src.Config as Config
from src.BlockGenerator import BlockGenerator
from src.Game import Game
from src.GameField import GameField
from src.Player import Player


class TetrisGame(Game):
    def __init__(self):
        self.game_field = GameField()
        super().__init__()
        self.fps_font = None
        self.fps = 0
        self.block_speed = Config.BLOCK_SPEED
        self.generator = BlockGenerator()
        self.player1 = None
        self.blocks = [self.generator.generate(self.block_speed)]
        self.dead = False

    # Gets called at the start of the game
    def init(self, window_name, size):
        super().init(window_name, size)
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
            self.dead = True

    # Called every frame, dt is time between frames
    def loop(self, dt):
        self.fps = 0 if dt == 0 else int(1 / dt)

        keys = pygame.key.get_pressed()
        self.player1.update(dt, keys, self.blocks)

        self.blocks[len(self.blocks) - 1].move(dt, self.blocks[:-1])

    # Called after loop(), renders the game screen
    def render(self):
        self.surface.fill(Color.BLACK)

        self.game_field.render(self.surface)

        # paint_tile(self.surface, 20, 20, 128, 128, Color.RED)
        # paint_tile(self.surface, 20, 148, 128, 128, Color.GREEN)
        # paint_tile(self.surface, 148, 20, 128, 128, Color.BLUE)
        # paint_tile(self.surface, 148, 148, 128, 128, Color.MAGENTA)

        # paint_tile(self.surface, 256, 256, 32, 32, Color.RED)

        for block in self.blocks:
            block.render(self.surface)

        self.player1.render(self.surface)

        # self.emitter.render(self.surface)

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        if self.dead:
            self.surface.blit(self.wasted_surface, (0, 50))

        pygame.display.update()
