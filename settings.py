class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 150, 180)
        self.ship_limit = 3  

        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speed_upscale = 1
        self.score_scale = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_upscale
        self.bullet_speed *= self.speed_upscale
        self.alien_speed *= self.speed_upscale
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)