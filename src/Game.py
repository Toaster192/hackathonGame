import pygame


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.surface = None
        self.running = False
        self.size = (0, 0)

    def init(self, window_name, size):
        self.size = size

        pygame.init()
        pygame.display.init()
        self.surface = pygame.display.set_mode(
            size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(window_name)

        pygame.font.init()

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
        while self.running:
            for event in pygame.event.get():
                self._handle_event(event)
            self.loop(self.clock.get_time()/1000)
            self.render()
            self.clock.tick(60)
        self._clean_up()
