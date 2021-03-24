class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.dead_aliens = 0
        self.ship_dead = 0
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit