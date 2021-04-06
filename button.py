import pygame.font
from random import randint

class Button():

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.msg = msg

        self.width, self.height = 200, 50
        self.button_color = (245, 66, 66)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self._rect_position()
        self._prep_msg()

    def _rect_position(self):    
        self.rect.center = self.screen_rect.center
    


    def _prep_msg(self):
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self._label_position()
        
      

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _label_position(self):
        self.msg_image_rect.center = self.rect.center



class LevelButton(Button):

    def __init__(self, ai_game, msg, level):
        self.level = level

        super().__init__(ai_game, msg)
        
        #self.msg_image_rect.midleft = (27, 540)
    def setclicked(self):
        self.msg_image = self.font.render(self.msg, True, (5,0,0), self.button_color)


    def setunclicked(self):
         self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)


    def _rect_position(self):
         self.rect.midleft = self.screen_rect.midleft
         button_pos = self.rect.midleft
         #print(button_pos)
         self.rect.midleft = (button_pos[0] + 5, button_pos[1]+140 + ((self.rect.height + 20) * (self.level-1)))
         #print(self.level)
         #print(self.rect.midleft)

        
    def _label_position(self):
    
        button_width = self.rect.width 
        label_width = self.msg_image_rect.width
        margin_x = int((button_width - label_width)/2)
        margin_y = self.msg_image_rect
        button_pos = self.rect.midleft
        self.msg_image_rect.midleft = (button_pos[0]+ margin_x,button_pos[1])

       # print(button_width, label_width, margin_x, button_pos)
      
     