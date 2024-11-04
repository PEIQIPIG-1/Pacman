import pygame


class Resources():
    # Class that stores resources, images, sounds and so on
    def __init__(self):
        self._load_ghost_images()
        self._load_pacman_images()
        self._load_sounds()

    def _load_ghost_images(self):
        self.ghost_images = {'blue_ghost_moving_right': [pygame.image.load('../images/ghost_sprites/blue_ghost_right'
                                                                           + str(i) + '.png') for i in range(1, 4)],
                             'blue_ghost_moving_left': [pygame.image.load('../images/ghost_sprites/blue_ghost_left'
                                                                          + str(i) + '.png') for i in range(1, 4)],
                             'blue_ghost_moving_up': [pygame.image.load('../images/ghost_sprites/blue_ghost_up'
                                                                        + str(i) + '.png') for i in range(1, 4)],
                             'blue_ghost_moving_down': [pygame.image.load('../images/ghost_sprites/blue_ghost_down'
                                                                          + str(i) + '.png') for i in range(1, 4)]}

    def _load_pacman_images(self):
        self.pacman_images = {'pacman_moving': [pygame.image.load('../images/pacman_sprites/pacman'
                                                                  + str(i) + '.png') for i in range(1, 4)]}

    def _load_sounds(self):
        self.sounds = {
            'beginning': pygame.mixer.Sound('../sounds/beginning.wav'),
            'eat_bean': pygame.mixer.Sound('../sounds/eat_bean.mp3'),
            'death': pygame.mixer.Sound('../sounds/death.wav'),
            'eat_fruit': pygame.mixer.Sound('../sounds/eat_fruit.wav'),
            'eat_ghost': pygame.mixer.Sound('../sounds/eat_ghost.wav'),
            'extra_pac': pygame.mixer.Sound('../sounds/extra_pac.wav'),
            'bgm': pygame.mixer.Sound('../sounds/intermission.wav'),
            
        }
        pygame.mixer.music.set_volume(0.5)
