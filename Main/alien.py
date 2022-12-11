import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас прибульця"""
    def __init__(self, ai_game):
        """Ініціалізація"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Загрузити картинку
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()

        #Спавнити справа зверху
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Зберігати поточну позицію
        self.x = float(self.rect.x)

    def update(self):
        """Змістити прибульця праворуч чи ліворуч"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Повертає істину, якщо прибулець на краю екрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right or self.rect.left<=0:
            return True


