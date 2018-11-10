import pygame
import src.Colors as Color

class Menu:

    def __init__(self):
        self.menu_font = pygame.font.Font('FreeMono.ttf', 16)

    def show(self, surface):
        pocet_hracu = \
            self.menu_font.render("How many players?", True, Color.GRAY)
        surface.blit(pocet_hracu, (0, 0))
        pygame.display.update()

        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.event.Event(pygame.QUIT, {"ev": "ev"})
                    return 0
                if event.type == pygame.KEYDOWN:
                    print(pygame.key.name(event.key)[1])
                    try:
                        return int(pygame.key.name(event.key)[1])
                    except:
                        pass
            pygame.time.Clock().tick(60)
