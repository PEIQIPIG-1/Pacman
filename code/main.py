import sys
import pygame
from settings import Settings


class Pacman:
    """Class that manages game resources and actions"""
    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Pacman")

    def run_game(self):
        """Start game main loop"""
        while True:
            # Listen to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Re-draw screen in each loop
            self.screen.fill(self.settings.bg_color)

            # Make screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Create game object and run the game
    pacman = Pacman()
    pacman.run_game()
