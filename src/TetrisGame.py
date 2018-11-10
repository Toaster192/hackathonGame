import pygame
from src.GameField import GameField
from src.Game import Game
import src.Colors as Color
import src.Config as Config
from src.Player import Player
from .Particles import ParticleFieldEmitter
from src.BlockGenerator import BlockGenerator
from .Vector import Vector2


class TetrisGame(Game):
    def __init__(self):
        self.game_field = GameField()
        super().__init__()
        self.fps_font = None
        self.fps = 0
        self.block_speed = (0, 150)
        self.generator = BlockGenerator()
        self.player1 = Player(51, 50, Config.PLAYER_WIDTH,
                              Config.PLAYER_HEIGHT, Color.RED)
        self.blocks = [self.generator.generate(self.block_speed)]

        self.emitter = ParticleFieldEmitter(
            colors=([Color.WHITE, Color.YELLOW, Color.ORANGE, Color.RED] + [
                Color.GRAY] * 2 + [Color.DARK_GRAY,
                                   Color.darker(Color.DARK_GRAY, 2),
                                   Color.BLACK]), pos=Vector2(256, 256),
            size=Vector2(32, 8), velocity=Vector2(16, -8),
            velocity_jitter=Vector2(4, 4), accel=Vector2(0, -4), gen_delay=0.01,
            duration=4, sizes=[3, 5, 8, 6, 8, 16])

    # Gets called at the start of the game
    def init(self, window_name, size):
        super().init(window_name, size)
        self.fps_font = pygame.font.Font('FreeMono.ttf', 16)

    # Gets called at game end (pressed [X])
    def clean_up(self):
        pass

    # Gets called on PyGame event
    def handle_event(self, event):
        print(event)
        if event.type == pygame.USEREVENT:
            self.blocks.append(self.generator.generate(self.block_speed))

    # Called every frame, dt is time between frames
    def loop(self, dt):
        self.fps = 0 if dt == 0 else int(1 / dt)

        keys = pygame.key.get_pressed()
        self.player1.update(dt, keys)

        self.blocks[len(self.blocks) - 1].move(dt, self.blocks[:-1])

        # self.emitter.update(dt)

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

        pygame.display.update()
