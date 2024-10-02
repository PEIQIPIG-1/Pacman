import pygame
from pygame.sprite import Sprite


class Pacman(Sprite):
    """Class that manages pacman"""

    def __init__(self, game, location=(0, 0)):
        """Initialize pacman"""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        # Load pacman images for animation
        self.images = game.resources.pacman_images
        self.rect = self.images['pacman_moving'][0].get_rect()

        # Initialize pacman at the mid-bottom of the screen
        self.rect.x = location[0] * self.settings.block_size + game.start_loc[0]
        self.rect.y = location[1] * self.settings.block_size + game.start_loc[1]

        # Store pacman's exact location
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Direction state of pacman
        self.direction = 'stop'
        self.next_direction = 'stop'

        # Animation attributes
        self.frame_index = 0  # Current frame index for animation
        self.animation_time = 100  # Time (in milliseconds) between frames
        self.last_update = pygame.time.get_ticks()  # Time of last frame update

    def update(self):
        # Update pacman's status
        self._update_pacman_direction()
        self._update_pacman_position()

    def _update_pacman_position(self):
        """Update pacman's position and animation and handle wall collisions"""
        # Save original location
        original_x = self.x
        original_y = self.y

        # Update pacman x location
        if self.direction == 'right':
            self.x += self.settings.pacman_speed
        elif self.direction == 'left':
            self.x -= self.settings.pacman_speed
        elif self.direction == 'up':
            self.y -= self.settings.pacman_speed
        elif self.direction == 'down':
            self.y += self.settings.pacman_speed

        # Update rect depends on self.x, self.y
        self.rect.x = self.x
        self.rect.y = self.y

        # Check if pacman collides with any wall
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.x = original_x
            self.rect.x = self.x
            self.y = original_y
            self.rect.y = self.y

        # Update animation frame
        self._update_pacman_animation()

    def _update_pacman_direction(self):
        """Update pacman's direction"""
        # Detect if pacman can turn to next direction
        detection_area = None
        if self.next_direction == 'stop':
            return
        elif self.next_direction == 'right':
            detection_area = pygame.Rect(self.rect.right, self.rect.top, 1, self.rect.height)
        elif self.next_direction == 'left':
            detection_area = pygame.Rect(self.rect.left - 1, self.rect.top, 1, self.rect.height)
        elif self.next_direction == 'up':
            detection_area = pygame.Rect(self.rect.left, self.rect.top - 1, self.rect.width, 1)
        elif self.next_direction == 'down':
            detection_area = pygame.Rect(self.rect.left, self.rect.bottom, self.rect.width, 1)
        if not pygame.sprite.spritecollideany(self, self.game.walls,
                                              collided=lambda pacman, wall: detection_area.colliderect(wall.rect)):
            self.direction = self.next_direction
            self.next_direction = 'stop'

    def _update_pacman_animation(self):
        """Update pacman's animation"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.animation_time:
            # Time to change the frame
            self.last_update = current_time
            self.frame_index = (self.frame_index + 1) % len(self.images['pacman_moving'])

    def blitme(self):
        """Draw pacman with animation"""
        # Get the current frame of the animation
        image = self.images['pacman_moving'][self.frame_index]

        # Rotate the image based on the direction Pacman is moving
        if self.direction == 'right':
            image = pygame.transform.rotate(image, 0)
        elif self.direction == 'left':
            image = pygame.transform.flip(image, True, False)
        elif self.direction == 'up':
            image = pygame.transform.rotate(image, 90)
        elif self.direction == 'down':
            image = pygame.transform.rotate(image, -90)

        self.screen.blit(image, self.rect)
