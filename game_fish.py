import pygame
import random
import game_common
class GameFish(object):
    def __init__(self):
        self.img = pygame.image.load('./res/fish.png')
        self.img_rect = self.img.get_rect()
        self.reset()
    def reset(self):
        self.img_rect[0] = random.randint(self.img_rect[2],
                                          game_common.WINDOW_WIDTH - self.img_rect[2] * 2)
        self.img_rect[1] = -self.img_rect[3]
        self.speed = random.randint(1, 2)
    def move_down(self):
        if self.img_rect[1] >= game_common.WINDOW_WIDTH:
            self.reset()
        self.img_rect.move_ip(0,self.speed)