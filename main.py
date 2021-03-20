import sys

import pygame


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Inwazja obcych")
        
        self.bg_color = (0, 0, 255)

    def run_game(self):
       while True:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   sys.exit()
                   
           self.screen.fill(bg_color) 

           pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
