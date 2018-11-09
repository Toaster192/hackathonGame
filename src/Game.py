import pygame
from time import time


class Game:
    def __init__(self):
        self.surface = None
        self.running = False
        self._time = 0

    def init_screen(self, size):
        pygame.init()
        self.surface = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def _clean_up(self):
        self.clean_up()
        pygame.quit()

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        self.handle_event(event)

    def clean_up(self):
        pass

    def handle_event(self, event):
        pass

    def loop(self, dt):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()

    def run(self):
        self.running = True
        self._time = time()
        while self.running:
            newtime = time()
            for event in pygame.event.get():
                self._handle_event(event)
            self.loop(newtime - self._time)
            self.render()
            self._time = newtime
        self._clean_up()
