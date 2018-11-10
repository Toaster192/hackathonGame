import pygame
from src.GameField import GameField
from src.Game import Game
import src.Colors as Color
import src.Config as Config
from src.TilePainter import paint_tile
from src.Player import Player
from .Particles import ParticleFieldEmitter
from src.Block import Block
import src.BlockTypes as BlockTypes
from src.BlockGenerator import BlockGenerator


class PlaceholderGame(Game):
    def __init__(self):
        self.game_field = GameField()
        super().__init__()
        self.fps_font = None
        self.fps = 0
        self.player1 = Player(50, 50, Config.PLAYER_WIDTH,
                              Config.PLAYER_HEIGHT, Color.RED)
        self.block = BlockGenerator.generate((0,50))

        self.emitter = ParticleFieldEmitter(color_begin=Color.GRAY,
                                            color_end=Color.BLACK,
                                            color_jitter=0.1, pos=(256, 256),
                                            size=(32, 8), velocity=(16, -8),
                                            velocity_jitter=(4, 4),
                                            accel=(0, -4), gen_delay=0.01,
                                            duration=4, size_begin=6,
                                            size_end=0)

    # Gets called at the start of the game
    def init(self, window_name, size):
        super().init(window_name, size)
        self.fps_font = pygame.font.Font('FreeMono.ttf', 16)

    # Gets called at game end (pressed [X])
    def clean_up(self):
        pass

    # Gets called on PyGame event
    def handle_event(self, event):
        pass

    # Called every frame, dt is time between frames
    def loop(self, dt):
        self.fps = 0 if dt == 0 else int(1 / dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            print(self.player1.x, Config.GAMEFIELD_LEFT_BORDER)
            self.player1.moveLeft()
            self.player1.left = True
            self.player1.right = False
            self.player1.facing = False
        if keys[pygame.K_RIGHT]:
            print(self.player1.x, Config.GAMEFIELD_RIGHT_BORDER)
            self.player1.moveRight()
            self.player1.left = False
            self.player1.right = True
            self.player1.facing = False
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.player1.stopMoving()
            self.player1.left = False
            self.player1.right = False
            self.player1.facing = True
        if keys[pygame.K_UP]:
            self.player1.jump()

        if (int(self.player1.x) <
                int(Config.GAMEFIELD_LEFT_BORDER) - self.player1.v_x):
            self.player1.v_x = 0
            self.player1.x = Config.GAMEFIELD_LEFT_BORDER
        elif (int(self.player1.x) >
                ((int(Config.GAMEFIELD_RIGHT_BORDER)) -
                    Config.PLAYER_WIDTH) - self.player1.v_x):
            self.player1.v_x = 0
            self.player1.x = (Config.GAMEFIELD_RIGHT_BORDER -
                              Config.PLAYER_WIDTH)

        if pygame.event.poll().type == pygame.USEREVENT:
            self.block = BlockGenerator.generate((0,50))
        self.player1.x += self.player1.v_x
        self.player1.y += self.player1.v_y

        self.block.move(dt)

        self.emitter.update(dt)

    # Called after loop(), renders the game screen

    def render(self):
        self.surface.fill(Color.BLACK)

        pygame.draw.rect(self.surface, self.player1.color, pygame.Rect(
            self.player1.x, self.player1.y,
            self.player1.width, self.player1.height))
        self.game_field.draw(self.surface)

        # paint_tile(self.surface, 20, 20, 128, 128, Color.RED)
        # paint_tile(self.surface, 20, 148, 128, 128, Color.GREEN)
        # paint_tile(self.surface, 148, 20, 128, 128, Color.BLUE)
        # paint_tile(self.surface, 148, 148, 128, 128, Color.MAGENTA)

        paint_tile(self.surface, 256, 256, 32, 32, Color.RED)

        self.block.draw(self.surface)
        pygame.draw.rect(self.surface, self.player1.color,
                         pygame.Rect(self.player1.x, self.player1.y,
                                     self.player1.width, self.player1.height))

        self.emitter.render(self.surface)

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        pygame.display.update()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self._handle_event(event)
            self.loop(self.clock.get_time() / 1000)
            self.render()
            self.clock.tick(60)
        self._clean_up()
