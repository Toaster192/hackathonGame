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
from src.Menu import Menu


class Data:
    def __init__(self, blocks, players):
        self.blocks = blocks
        self.players = list()
        for player in players:
            self.players.append((player.pos.x, player.pos.y, player.v.x, player.v.y))


class TetrisGame(Game):
    def __init__(self):
        self.game_field = GameField()
        super().__init__()
        self.fps_font = None
        self.fps = 0
        self.block_speed = Config.BLOCK_SPEED
        self.generator = BlockGenerator()
        self.players = []
        self.blocks = [self.generator.generate(self.block_speed)]
        self.sockets = list()
        self.connections = list()
        self.menu = None
        self.number_of_players = 0


    # Gets called at the start of the game
    def init(self, window_name, size):
        super().init(window_name, size)
        self.menu = Menu()
        #print(self.menu.show(self.surface))
        number_of_players = self.menu.show(self.surface)
        if number_of_players == 0:
            self.running = False
        for i in range(0, number_of_players):
            self.players.append(Player(Config.GAMEFIELD_LEFT_BORDER +
                              (Config.GAMEFIELD_WIDTH // 2),
                              Config.GAMEFIELD_BOTTOM_BORDER -
                              Config.PLAYER_HEIGHT, Config.PLAYER_WIDTH,
                              Config.PLAYER_HEIGHT, Color.RED))
        self.fps_font = pygame.font.Font('FreeMono.ttf', 16)
        host = "127.0.0.23"
        port = 12346
        print(self.players)
        self.sockets.append(s.socket())
        for i in range(0, number_of_players - 1):
            self.sockets[0].bind((host, port))
            self.sockets[0].listen(5)
            conn, neco = self.sockets[0].accept()
            self.connections.append(conn)
            print(i, " players connected")

        #self.socket_out.bind(("127.0.0.2", port))

    # Gets called at game end (pressed [X])
    def clean_up(self):
        for socket in self.sockets:
            socket.close()

    # Gets called on PyGame event
    def handle_event(self, event):
        # print(event)
        if event.type == pygame.USEREVENT:
            self.blocks.append(self.generator.generate(self.block_speed))

    # Called every frame, dt is time between frames
    def loop(self, dt):
        self.fps = 0 if dt == 0 else int(1 / dt)
        d = bytes()
        #if len(self.players) > 1:
            #dat = Data(self.blocks, self.players)
            #print(dat)
            #d = pickle.dumps(dat)
        print(pickle)
        for conn in self.connections:
            d = Data(self.blocks, self.players)
            conn.send(pickle.dumps(d, pickle.HIGHEST_PROTOCOL))
        for index, conn in enumerate(self.connections, 1):
            d = conn.recv(16000)
            if d is not None:
                self.players[index] = Player(Config.GAMEFIELD_LEFT_BORDER +
                              (Config.GAMEFIELD_WIDTH // 2),
                              Config.GAMEFIELD_BOTTOM_BORDER -
                              Config.PLAYER_HEIGHT, Config.PLAYER_WIDTH,
                              Config.PLAYER_HEIGHT, Color.RED)
                self.players[index].set_state(*pickle.loads(d).players[0])
        for i, player in enumerate(self.players):
            keys = pygame.key.get_pressed()
            if i == 0:
                player.update(dt, keys, self.blocks)
            else:
                player.update(dt, None, self.blocks)

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

        for player in self.players:
            player.render(self.surface)

        # self.emitter.render(self.surface)

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        pygame.display.update()
