import sys

import pygame

from settings import Settings
from pacman import Pacman
from ghost import Ghost
from level import Level
from wall import Wall
from bean import Bean
from game_stats import GameStats
from resources import Resources


class Game:
    """Class that manages game resources and actions"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.resources = Resources()

        # Full screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # Window mode
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Pacman")

        self.level_num = 1
        self.level = Level(self)
        self.distances_dist = {}
        self.start_loc = self.level.start_loc
        self.walls = pygame.sprite.Group()
        self.beans = pygame.sprite.Group()
        self.pacman = Pacman(self, self.level.pacman_loc)
        self.ghosts = pygame.sprite.Group()

        self._create_walls()
        self._create_beans()
        self._create_ghosts()

        # Store game stats
        self.stats = GameStats(self)

    def run_game(self):
        """Start game main loop"""
        while True:
            # Listen to keyboard and mouse events
            self._check_events()
            # Refresh pacman
            self.pacman.update()
            # Refresh beans
            self._update_beans()
            # Refresh ghosts
            self._update_ghosts()
            # Refresh screen
            self._update_screen()

    # def _initialize_distances_dict(self):

    def _create_walls(self):
        for wall_loc in self.level.walls_locs:
            wall = Wall(self, wall_loc)
            self.walls.add(wall)

    def _create_beans(self):
        for bean_loc in self.level.beans_locs:
            bean = Bean(self, bean_loc)
            self.beans.add(bean)

    def _create_ghosts(self):
        """Create ghost group"""
        for ghost_loc in self.level.ghosts_locs:
            ghost = Ghost(self, ghost_loc)
            self.ghosts.add(ghost)

    def _check_events(self):
        """Listen to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Keydown events"""
        if event.key == pygame.K_RIGHT:
            # Moving pacman right
            self.pacman.next_direction = 'right'
        elif event.key == pygame.K_LEFT:
            # Moving pacman left
            self.pacman.next_direction = 'left'
        elif event.key == pygame.K_UP:
            # Moving pacman up
            self.pacman.next_direction = 'up'
        elif event.key == pygame.K_DOWN:
            # Moving pacman down
            self.pacman.next_direction = 'down'

    def _check_keyup_event(self, event):
        """Keyup events"""
        if event.key == pygame.K_q:
            sys.exit()

    def _update_beans(self):
        """Update beans if they have been eaten"""
        # Check for collision between Pacman and beans
        collided_beans = pygame.sprite.spritecollide(self.pacman, self.beans, False)

        # If there is collided beans, pacman will eat them
        if collided_beans:
            for bean in collided_beans:
                # Remove the bean
                bean.kill()
                # Number of bean minus 1
                self.stats.beans_left -= 1
                # Get Score
                self.stats.score += self.settings.eat_bean_score

    def _update_ghosts(self):
        # Update ghosts' position
        self.ghosts.update()

        # Check collision between ghosts and pacman
        if pygame.sprite.spritecollideany(self.pacman, self.ghosts):
            self._pacman_eaten()

    def _pacman_eaten(self):
        """Response when pacman is eaten by ghost"""
        # Pacman's life-1
        self.stats.pacman_life -= 1
        # Update Score
        self.stats.score += self.settings.eaten_by_ghost_score
        # Reset ghosts
        self.ghosts.empty()
        self._create_ghosts()
        # Reset pacman
        self.pacman = Pacman(self, self.level.pacman_loc)

    def _update_screen(self):
        """Refresh screen"""
        # Re-draw screen
        self.screen.fill(self.settings.bg_color)
        self.walls.draw(self.screen)
        self.beans.draw(self.screen)
        self.pacman.blitme()
        self.ghosts.draw(self.screen)

        # Make new screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Create game object and run the game
    game = Game()
    game.run_game()
