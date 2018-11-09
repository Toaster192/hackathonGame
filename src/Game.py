import pygame


class Game:
    def __init__(self):
        self.surface = None
        self.running = False

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

    def loop(self):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self._handle_event(event)
            self.loop()
            self.render()
        self._clean_up()
