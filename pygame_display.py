import pygame

class Win:
    def __init__(self):
        #iniciar el motor pygame
        self.engine_init = pygame.init()
        self.resolution = (800,600)
        pygame.display.init()
        pygame.display.set_caption('window')
        self.screen = pygame.display.set_mode(self.resolution)

    def evento_loop():
        # evento para cerrar el display 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


initialize = Win()
Win.evento_loop()

