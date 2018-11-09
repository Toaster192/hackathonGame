import pygame
from src.Game import Game
import src.Colors as Color


class PlaceholderGame(Game):
    def __init__(self):
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
        self.fps = 0 if dt == 0 else int(1000 / dt)

    # Called after loop(), renders the game screen
    def render(self):
        self.surface.fill(Color.BLACK)

        fps_surface = \
            self.fps_font.render('FPS: ' + str(self.fps), True, Color.GRAY)
        self.surface.blit(fps_surface, (0, 0))

        pygame.display.update()
