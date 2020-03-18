import pygame
import game_common
class GameCat(object):

    def __init__(self):
        self.img = pygame.image.load('./res/cat.png')
        self.img_rect = self.img.get_rect()
        self.img_rect[0] = (game_common.WINDOW_WIDTH - self.img_rect[2])/2
        self.img_rect[1] = (game_common.WINDOW_HEIGHT - self.img_rect[3])

    def move(self,pos):
        pos_x = pos[0]
        if pos_x > game_common.WINDOW_WIDTH - self.img_rect[2]:
            pos_x = game_common.WINDOW_WIDTH - self.img_rect[2]
        self.img_rect[0] = pos_x
