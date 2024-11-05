import pygame
from pygame.sprite import Sprite


class Bean(Sprite):

    def __init__(self, game, location=(0, 0)):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.bean_size = self.settings.bean_size
        self.block_size = self.settings.block_size
        # Load ghost images and set their rect attributes
        self.image = game.resources.images['bean'][0]
        self.rect = self.image.get_rect()

        # Set ghost's location
        self.rect.x = location[0] * self.block_size + game.start_loc[0] + (self.block_size - self.bean_size) / 2
        self.rect.y = location[1] * self.block_size + game.start_loc[1] + (self.block_size - self.bean_size) / 2


