class Level:
    """Class that represents single ghost"""

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        # Load levels
        self.walls_locs = []
        self.ghosts_locs = []
        self.beans_locs = []
        self.pacman_loc = None
        self.start_loc = (0, 0)
        self.load_level(game.level_num)

    def load_level(self, level_num):
        with open('../levels/level' + str(level_num) + '.txt', 'r') as file:
            lines = file.readlines()

        self.start_loc = ((self.settings.screen_width - len(lines[0].strip()) * self.settings.block_size) / 2,
                          (self.settings.screen_height - len(lines) * self.settings.block_size) / 2)

        for row, line in enumerate(lines):
            for col, c in enumerate(line):
                if c == '%':
                    self.walls_locs.append((col, row))
                elif c == '.':
                    self.beans_locs.append((col, row))
                elif c == 'W' or c == 'X' or c == 'Y' or c == 'Z':
                    self.ghosts_locs.append((col, row))
                elif c == 'P':
                    self.pacman_loc = (col, row)

