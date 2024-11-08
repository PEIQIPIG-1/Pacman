class Settings:
    """Storage all settings in Pacman"""

    def __init__(self):
        """Initialize settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Map block size
        self.block_size = 32

        # Pacman settings
        self.pacman_speed = 1
        self.pacman_life = 3

        # Ghost settings
        self.ghost_speed = 0.5
        self.ghost_num = 4

        # Bean settings
        self.bean_size = 16

        # Score settings
        self.eat_bean_score = 10
        self.eaten_by_ghost_score = -500
