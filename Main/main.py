import pygame

class AlienInvasion:
    """Основний клас"""
    def __init__(self):
        """Ініціалізація"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Головний цикл"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()