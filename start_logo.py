import pygame
import game_common

class StartLogo(object):
    def __init__(self):
        self.img = pygame.image.load('./res/logo.png')
        self.img_rect = self.img.get_rect()
        #<rect(0,0,400,300)> (x,y,w,h)
        print(self.img_rect)
        self.img_rect[0] = (game_common.WINDOW_WIDTH - self.img_rect[2])/2
        self.img_rect[1] = 60