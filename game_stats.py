class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.dead_aliens = 0
        self.ship_dead = 0
        self.high_score = self.open_txt()
        

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def open_txt(self):
        with open ('wyniki.txt') as file_object:
            high_score = file_object.read()
            return int(high_score)
