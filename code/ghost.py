import pygame
from pygame.sprite import Sprite


class Ghost(Sprite):
    """Class that represents single ghost"""

    def __init__(self, game, location=(0, 0)):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load ghost images and set their rect attributes
        self.image = pygame.image.load('../images/ghost_sprites/blue_ghost_left1.png')
        self.rect = self.image.get_rect()

        # Set ghost's location
        self.rect.x = location[0] * self.settings.block_size + game.start_loc[0]
        self.rect.y = location[1] * self.settings.block_size + game.start_loc[1]

        # Store ghost's exact location
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Moving ghosts"""
        # self.x += self.settings.ghost_speed
        # self.rect.x = self.x
