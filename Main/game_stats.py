class GameStats:
    """Відстеження статистики"""
    def __init__(self, ai_game):
        """Ініціалізація"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Ініціалізація статистики, що може мінятись по ходу гри"""
        self.ship_left = self.settings.ship_limit
        self.score = 0