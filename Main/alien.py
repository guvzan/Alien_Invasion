import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас прибульця"""
    def __init__(self, ai_game):
        """Ініціалізація"""
        super.__init__()
        self.screen = ai_game.screen

        #Загрузити картинку
        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()

        #Спавнити справа зверху
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Зберігати поточну позицію
        self.x = float(self.rect.x)