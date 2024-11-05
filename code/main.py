import pygame

from settings import Settings
from game_stats import GameStats
from resources import Resources
from levels.level1.level1 import Level1
from main_menu import MainMenu


class Game:
    """Class that manages game resources and actions"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.resources = Resources()

        # Window mode
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height),
            pygame.NOFRAME
        )

        self.clock = pygame.time.Clock()
        self.start = False
        self.level_lists = [MainMenu, Level1, Level1, Level1]
        with open('../save.txt', 'r') as file:
            self.level_num = int(file.readlines()[0])
        self.level = self.level_lists[self.level_num](self)
        self.main_menu = MainMenu(self)
        # Store game stats
        # self.stats = GameStats(self)

    def run_game(self):
        """Start game main loop"""
        while True:
            self.clock.tick(60)
            self.main_menu.run_menu()
            while self.start:
                self.clock.tick(60)
                self.level.run_level()

    def _render_text(self, text, font_size, color):
        font = pygame.font.Font(self.resources.font_path, font_size)  # Create the font with the new size
        text_surface = font.render(text, True, color)  # Render the text
        return text_surface


if __name__ == '__main__':
    # Create game object and run the game
    game = Game()
    game.run_game()
