import pygame
from src.GameField import GameField
from src.Game import Game
import src.Colors as Color
from src.TilePainter import paint_tile


class PlaceholderGame(Game):
    def __init__(self):
        self.game_field = GameField()
        super().__init__()
        self.fps_font = None
        self.fps = 0

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

    # Called after loop(), renders the game screen
    def render(self):
        self.surface.fill(Color.BLACK)
        self.game_field.draw(self.surface)

        paint_tile(self.surface, 20, 20, 128, 128, Color.RED)
        paint_tile(self.surface, 20, 148, 128, 128, Color.GREEN)
        paint_tile(self.surface, 148, 20, 128, 128, Color.BLUE)
        paint_tile(self.surface, 148, 148, 128, 128, Color.MAGENTA)

        paint_tile(self.surface, 60, 300, 16, 16, Color.ORANGE)

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        pygame.display.update()
