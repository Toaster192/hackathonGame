import pygame

import src.Colors as Color
import src.Config as Config
from src.BlockGenerator import BlockGenerator
from src.Game import Game
from src.GameField import GameField
from src.Player import Player
from .Vector import Vector2
import socket as s
import pickle

class Data:
    def __init__(self, blocks, player):
        self.blocks = blocks
        self.player = player

class TetrisGame(Game):
    def __init__(self):
        self.game_field = GameField()
        super().__init__()
        self.fps_font = None
        self.fps = 0
        self.block_speed = Config.BLOCK_SPEED
        self.generator = BlockGenerator()
        self.player1 = None
        self.player2 = None
        self.blocks = [self.generator.generate(self.block_speed)]
        self.socket = s.socket()
        self.socket_out = s.socket()
        self.smth = None


    # Gets called at the start of the game
    def init(self, window_name, size):
        super().init(window_name, size)
        self.player1 = Player(Config.GAMEFIELD_LEFT_BORDER +
                              (Config.GAMEFIELD_WIDTH // 2),
                              Config.GAMEFIELD_BOTTOM_BORDER -
                              Config.PLAYER_HEIGHT, Config.PLAYER_WIDTH,
                              Config.PLAYER_HEIGHT, Color.RED)
        self.fps_font = pygame.font.Font('FreeMono.ttf', 16)
        host = "127.0.0.5"
        port = 12345
        self.socket.bind((host, port))
        self.socket.listen(5)
        self.smth, neco = self.socket.accept()

        #self.socket_out.bind(("127.0.0.2", port))

    # Gets called at game end (pressed [X])
    def clean_up(self):
        self.socket.close()

    # Gets called on PyGame event
    def handle_event(self, event):
        # print(event)
        if event.type == pygame.USEREVENT:
            self.blocks.append(self.generator.generate(self.block_speed))

    # Called every frame, dt is time between frames
    def loop(self, dt):
        self.fps = 0 if dt == 0 else int(1 / dt)
        d = Data(self.blocks, self.player1)
        self.smth.send(pickle.dumps(d))
        d = pickle.loads(self.smth.recv(16000))
        self.player2 = d.player
        keys = pygame.key.get_pressed()
        self.player1.update(dt, keys, self.blocks)
        self.player2.update(dt, keys, self.blocks)

        for i, block in enumerate(self.blocks):
            if block.falling:
                block.move(dt, self.blocks[:i] + self.blocks[i+1:],
                           Config.SCREEN_HEIGHT // Config.BLOCKS_FALLING)

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
        self.player2.render(self.surface)

        # self.emitter.render(self.surface)

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        pygame.display.update()
