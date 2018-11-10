import pygame
from src.GameField import GameField
from src.Game import Game
import src.Colors as Color
import src.Config as Config
# from src.TilePainter import paint_tile
from src.Player import Player


class PlaceholderGame(Game):

    def __init__(self):
        self.game_field = GameField()
        super().__init__()
        self.fps_font = None
        self.fps = 0
        self.player1 = Player((Config.SCREEN_WIDTH) // 2,
                              Config.GAMEFIELD_BOTTOM_BORDER -
                              Config.PLAYER_HEIGHT,
                              Config.PLAYER_WIDTH,
                              Config.PLAYER_HEIGHT, Color.RED)

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
            if int(self.player1.x) <= int(Config.GAMEFIELD_LEFT_BORDER) + 1:
                self.player1.v_x = 0
                self.player1.x = Config.GAMEFIELD_LEFT_BORDER
            else:
                self.player1.moveLeft()
        if keys[pygame.K_RIGHT]:
            print(Config.PLAYER_WIDTH)
            if int(self.player1.x) >= ((int(Config.GAMEFIELD_RIGHT_BORDER) - 1) - Config.PLAYER_WIDTH):
                self.player1.v_x = 0
                self.player1.x = Config.GAMEFIELD_RIGHT_BORDER - Config.PLAYER_WIDTH
            else:
                self.player1.moveRight()
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.player1.stopMoving()
        if keys[pygame.K_UP]:
            self.player1.jump()

        self.player1.x += self.player1.v_x
        self.player1.y += self.player1.v_y

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

        # paint_tile(self.surface, 60, 300, 16, 16, Color.ORANGE)

        pygame.draw.rect(self.surface, self.player1.color,
                         pygame.Rect(self.player1.x, self.player1.y,
                                     self.player1.width, self.player1.height))

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        pygame.display.update()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self._handle_event(event)
            self.loop(self.clock.get_time()/1000)
            self.render()
            self.clock.tick(60)
        self._clean_up()
