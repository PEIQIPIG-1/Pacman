import pygame
from pygame.sprite import Sprite
from collections import deque


class Ghost(Sprite):
    """Class that represents single ghost"""

    def __init__(self, game, location=(0, 0)):
        """Initialize the ghost"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.game = game

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
        """Move ghosts toward pacman"""
        self._move_towards_pacman()

    def _move_towards_pacman(self):
        """Move the ghost using BFS to find the shortest path to pacman"""
        pacman = self.game.pacman

        original_x = self.x
        original_y = self.y

        # Calculate the difference between Ghost's position and Pacman's position
        dx = pacman.rect.x - self.rect.x
        dy = pacman.rect.y - self.rect.y

        # Normalize the direction vector
        if dx != 0:
            dx = self.settings.ghost_speed if dx > 0 else -self.settings.ghost_speed
        if dy != 0:
            dy = self.settings.ghost_speed if dy > 0 else -self.settings.ghost_speed

        # Update ghost's position
        self.x += dx
        self.rect.x = self.x
        # Check if pacman collides with any wall
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.x = original_x
            self.rect.x = self.x

        self.y += dy
        self.rect.y = self.y
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.y = original_y
            self.rect.y = self.y
