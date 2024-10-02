import pygame


class Resources():
    # Class that stores resources, images, sounds and so on
    def __init__(self):
        self._load_ghost_images()
        self._load_pacman_images()

    def _load_ghost_images(self):
        self.ghost_images = {'blue_ghost_moving_right': [pygame.image.load('../images/ghost_sprites/blue_ghost_left'
                                                                           + str(i) + '.png') for i in range(1, 3)],
                             'blue_ghost_moving_left': [pygame.image.load('../images/ghost_sprites/blue_ghost_left'
                                                                          + str(i) + '.png') for i in range(1, 3)],
                             'blue_ghost_moving_up': [pygame.image.load('../images/ghost_sprites/blue_ghost_left'
                                                                        + str(i) + '.png') for i in range(1, 3)],
                             'blue_ghost_moving_down': [pygame.image.load('../images/ghost_sprites/blue_ghost_left'
                                                                          + str(i) + '.png') for i in range(1, 3)]}

    def _load_pacman_images(self):
        self.pacman_images = {'pacman_moving': [pygame.image.load('../images/pacman_sprites/pacman'
                                                                  + str(i) + '.png') for i in range(1, 4)]}
