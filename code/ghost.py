import pygame
from pygame.sprite import Sprite
from collections import deque


class Ghost(Sprite):
    """Class that represents single ghost"""

    def __init__(self, game, position=(0, 0)):
        """Initialize the ghost"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.game = game

        # Load ghost images and set their rect attributes
        self.images = game.resources.ghost_images
        self.image = self.images['blue_ghost_moving_left'][0]
        self.rect = self.image.get_rect()

        # Set ghost's position
        self.rect.x = position[0] * self.settings.block_size + game.start_loc[0]
        self.rect.y = position[1] * self.settings.block_size + game.start_loc[1]
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Ghost's speed and direction
        self.speed = self.settings.ghost_speed
        self.target_position = None  # Target position based on BFS
        self.direction = 'left'

        # Animation attributes
        self.frame_index = 0  # Current frame index for animation
        self.animation_time = 100  # Time (in milliseconds) between frames
        self.last_update = pygame.time.get_ticks()  # Time of last frame update

    def update(self):
        """Update ghost's status"""
        if self.target_position is None or self._reached_target():
            # If the ghost has no target or reached its current target, calculate new path
            self._calculate_path()

        self._move_to_pacman()

        # Update animation frame
        self._update_ghost_animation()

    def _reached_target(self):
        """Check if the ghost has reached the current target position"""
        return abs(self.x - self.target_position[0]) < self.speed and abs(self.y - self.target_position[1]) < self.speed

    def _calculate_path(self):
        """Use BFS to calculate the shortest path from ghost to pacman on the grid"""
        # Get the grid coordinates of the ghost and pacman
        ghost_grid_pos = self._get_grid_position(self.rect.x, self.rect.y)
        pacman_grid_pos = self._get_grid_position(self.game.pacman.rect.x, self.game.pacman.rect.y)

        # Perform BFS on grid to find the shortest path
        path = self._bfs(ghost_grid_pos, pacman_grid_pos)

        if path:
            # Get the next target position in pixels
            next_grid_pos = path[0]  # First step in the path
            self.target_position = self._get_pixel_position(next_grid_pos)

    def _bfs(self, start, goal):
        """Breadth-First Search to find the shortest path from start to goal on the grid"""
        walls = set(self._get_grid_position(wall.rect.x, wall.rect.y) for wall in self.game.walls)
        queue = deque([start])
        came_from = {start: None}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left

        while queue:
            current = queue.popleft()

            if current == goal:
                break

            for d in directions:
                neighbor = (current[0] + d[0], current[1] + d[1])

                if neighbor not in walls and neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

        # Reconstruct the path
        path = []
        current = goal
        while current != start:
            if current not in came_from:
                return []  # No valid path
            path.append(current)
            current = came_from[current]

        path.reverse()
        return path  # Return the list of steps to follow

    def _move_to_pacman(self):
        """Move ghost toward the current target position"""
        if self.target_position:
            dx = self.target_position[0] - self.x
            dy = self.target_position[1] - self.y

            if abs(dx) > abs(dy):  # Prioritize horizontal movement
                if dx > 0:
                    self.direction = 'right'
                    self.x += self.speed
                else:
                    self.direction = 'left'
                    self.x -= self.speed

            else:  # Vertical movement
                if dy > 0:
                    self.direction = 'down'
                    self.y += self.speed
                else:
                    self.direction = 'up'
                    self.y += -self.speed

            # Update the ghost's rect position
            self.rect.x = self.x
            self.rect.y = self.y

    def _update_ghost_animation(self):
        """Update ghost's animation"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.animation_time:
            # Time to change the frame
            self.last_update = current_time
            self.frame_index = (self.frame_index + 1) % len(self.images['blue_ghost_moving_' + self.direction])
            self.image = self.images['blue_ghost_moving_' + self.direction][self.frame_index]

    def _get_grid_position(self, x, y):
        """Convert pixel position to grid position considering start_loc and coordinate inversion"""
        grid_x = int((x - self.game.start_loc[0]) // self.settings.block_size)
        grid_y = int((y - self.game.start_loc[1]) // self.settings.block_size)
        return grid_y, grid_x  # Reverse x and y to match the map indexing

    def _get_pixel_position(self, grid_pos):
        """Convert grid position back to pixel position considering start_loc"""
        grid_y, grid_x = grid_pos  # Reverse back to normal pygame coordinates
        pixel_x = grid_x * self.settings.block_size + self.game.start_loc[0]
        pixel_y = grid_y * self.settings.block_size + self.game.start_loc[1]
        return pixel_x, pixel_y






