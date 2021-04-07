import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
       
        self.rect = self.image.get_rect()
        

        self.rect.midbottom = self.screen_rect.midbottom
        print('const')
        print(self.rect)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def make_small(self):
        #robi mały statek - żyćko
         self.image = pygame.transform.scale(self.image, (50,59))
         self.rect = self.image.get_rect()

    def update(self):
        # położenie statku
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # wyswietalnie statku na ekranie
        self.screen.blit(self.image, self.rect)
