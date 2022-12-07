import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Основний клас"""
    def __init__(self):
        """Ініціалізація"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """Головний цикл"""
        while True:
            self._check_events()
            self._update_screen()




    def _check_events(self):
        """Диспетчер подій"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 10

    def _update_screen(self):
        """Оновлення екрану"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()