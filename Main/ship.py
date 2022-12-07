import pygame

class Ship:
    """Клас корабля"""

    def __init__(self, ai_game):
        """Ініціалізація"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Оновити позицію корабля"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Намалювати корабель"""
        self.screen.blit(self.image, self.rect)