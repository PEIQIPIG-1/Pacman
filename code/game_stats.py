class GameStats():
    """Store game statistical information"""
    def __init__(self, game):
        """Initialize statistical information"""
        self.game = game
        self.settings = game.settings
        self._reset_stats()

    def _reset_stats(self):
        """Initialize information that may be changed during game"""
        self.score = 0
        self.beans_left = len(self.game.beans)


