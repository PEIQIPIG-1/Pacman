import pygame
from levels.level1.pacman import Pacman
from levels.level1.wall import Wall
from levels.level1.ghost import Ghost
from levels.level1.bean import Bean
from resources import Resources
import sys


class Level1:

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        # Load levels
        self.walls_locs = []
        self.ghosts_locs = []
        self.beans_locs = []
        self.pacman_loc = None
        self.start_loc = (0, 0)
        self.distances_dict = {}
        self.resources = Resources(1)

        self.load_level()

        self.walls = pygame.sprite.Group()
        self.beans = pygame.sprite.Group()
        self.pacman = Pacman(self, self.pacman_loc)
        self.ghosts = pygame.sprite.Group()

        self.beans_left = len(self.beans)
        self._create_walls()
        self._create_beans()
        self._create_ghosts()

    def load_level(self):
        with open('../levels/level1.txt', 'r') as file:
            lines = file.readlines()

        self.start_loc = ((self.settings.screen_width - len(lines[0].strip()) * self.settings.block_size) / 2,
                          (self.settings.screen_height - len(lines) * self.settings.block_size) / 2)

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '%':
                    self.walls_locs.append((x, y))
                elif c == '.':
                    self.beans_locs.append((x, y))
                elif c == 'W' or c == 'X' or c == 'Y' or c == 'Z':
                    self.ghosts_locs.append((x, y))
                elif c == 'P':
                    self.pacman_loc = (x, y)

    def _create_walls(self):
        for wall_loc in self.walls_locs:
            wall = Wall(self, wall_loc)
            self.walls.add(wall)

    def _create_beans(self):
        for bean_loc in self.beans_locs:
            bean = Bean(self, bean_loc)
            self.beans.add(bean)

    def _create_ghosts(self):
        """Create ghost group"""
        for ghost_loc in self.ghosts_locs:
            ghost = Ghost(self, ghost_loc)
            self.ghosts.add(ghost)

    def _check_events(self):
        """Listen to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            # elif event.type == pygame.KEYUP:
            #     self._check_keyup_event(event)

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

    # def _check_keyup_event(self, event):
    #     """Keyup events"""
    #     if event.key == pygame.K_q:
    #         sys.exit()

    def _update_beans(self):
        """Update beans if they have been eaten"""
        # Check for collision between Pacman and beans
        collided_beans = pygame.sprite.spritecollide(self.pacman, self.beans, False)

        # If there is collided beans, pacman will eat them
        if collided_beans:
            for bean in collided_beans:
                # Play sound
                self.resources.sounds['eat_bean'].play()
                # Remove the bean
                bean.kill()
                # Number of bean minus 1
                self.beans_left -= 1

    def _update_ghosts(self):
        # Update ghosts' position
        self.ghosts.update()

        # Check collision between ghosts and pacman
        if pygame.sprite.spritecollideany(self.pacman, self.ghosts):
            self._pacman_eaten()

    def _pacman_eaten(self):
        """Response when pacman is eaten by ghost"""
        # Reset ghosts
        self.ghosts.empty()
        self._create_ghosts()
        # Reset pacman
        self.pacman = Pacman(self, self.pacman_loc)

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

    def run_level(self):
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
