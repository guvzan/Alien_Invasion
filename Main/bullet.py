import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Клас кулі"""

    def __init__(self, ai_game):
        """Ініціалізація"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Створити rect кулі у (0, 0) та задати правильну позицію
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Зберігати позицію кулі як десяткове значення
        self.y = float(self.rect.y)

    def update(self):
        """Оновити позицію кулі"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Намалювати кулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)