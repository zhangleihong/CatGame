import pygame
import game_common
import random
class StartText(object):

    def __init__(self):
        self.font = pygame.font.SysFont('SimHei',34)
        self.text = self.font.render('点击开始',True,(255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect[0] = (game_common.WINDOW_WIDTH - self.text_rect[2])/2
        self.text_rect[1] = 400

class ScoreText(object):

    def __init__(self):
        self.font = pygame.font.SysFont('SimHei', 25)
        self.num = 0
        self.text = self.font.render('分数：%d' %self.num, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect[0] = 10
        self.text_rect[1] = 10

    def set_text(self):
        self.num += 10
        r = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.text = self.font.render('分数：%d' % self.num, True, (r, g, b))

