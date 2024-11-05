import pygame


class Resources():
    # Class that stores resources, images, sounds and so on
    def __init__(self, level=0):
        self._load_images(level)
        self._load_sounds(level)
        self._load_font(level)

    def _load_images(self, level):
        if level == 1:
            self.images = {'blue_ghost_moving_right': [pygame.image.load('../images/ghost_sprites/blue_ghost_right'
                                                                         + str(i) + '.png') for i in range(1, 4)],
                           'blue_ghost_moving_left': [pygame.image.load('../images/ghost_sprites/blue_ghost_left'
                                                                        + str(i) + '.png') for i in range(1, 4)],
                           'blue_ghost_moving_up': [pygame.image.load('../images/ghost_sprites/blue_ghost_up'
                                                                      + str(i) + '.png') for i in range(1, 4)],
                           'blue_ghost_moving_down': [pygame.image.load('../images/ghost_sprites/blue_ghost_down'
                                                                        + str(i) + '.png') for i in range(1, 4)],
                           'pacman_moving': [pygame.image.load('../images/pacman_sprites/pacman' + str(i) + '.png'
                                                               ) for i in range(1, 4)],
                           'wall': [pygame.image.load('../images/wall_sprites/wall.png')],
                           'bean': [pygame.image.load('../images/bean_sprites/bean.png')]}

    def _load_sounds(self, level):
        if level == 0:
            self.sounds = {
                'button_beep': pygame.mixer.Sound('../sounds/menu/button_beep.wav')
            }
        if level == 1:
            self.sounds = {
                'beginning': pygame.mixer.Sound('../sounds/level1/beginning.wav'),
                'eat_bean': pygame.mixer.Sound('../sounds/level1/eat_bean.mp3'),
                'death': pygame.mixer.Sound('../sounds/level1/death.wav'),
                'eat_fruit': pygame.mixer.Sound('../sounds/level1/eat_fruit.wav'),
                'eat_ghost': pygame.mixer.Sound('../sounds/level1/eat_ghost.wav'),
                'extra_pac': pygame.mixer.Sound('../sounds/level1/extra_pac.wav'),
                'bgm': pygame.mixer.Sound('../sounds/level1/intermission.wav'),

            }
        pygame.mixer.music.set_volume(0.5)

    def _load_font(self, level):
        self.font_path = "../font/menu_font.ttf"
