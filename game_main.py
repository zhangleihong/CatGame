import pygame
import game_common
import start_logo
import game_text
import game_map
import game_fish
import game_cat
class GameWindow(object):

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode([game_common.WINDOW_WIDTH,game_common.WINDOW_HEIGHT])
        pygame.display.set_caption("猫吃鱼")
        icon_img = pygame.image.load('./res/app.ico')

        pygame.display.set_icon(icon_img)
        self.start_logo = start_logo.StartLogo()
        self.game_text = game_text.StartText()
        self.is_start = False
        self.game_map = game_map.GameMap()
        self.game_fish = game_fish.GameFish()
        self.game_cat = game_cat.GameCat()
        self.game_score = game_text.ScoreText()
    def draw(self):
        if self.is_start == False:
            self.window.blit(self.start_logo.img,(self.start_logo.img_rect[0],
                                                  self.start_logo.img_rect[1]))
            self.window.blit(self.game_text.text, (self.game_text.text_rect[0],
                                                   self.game_text.text_rect[1]))
        else:
            self.window.blit(self.game_map.img,(0,0))
            self.window.blit(self.game_fish.img,(self.game_fish.img_rect[0],
                                                 self.game_fish.img_rect[1]))
            self.window.blit(self.game_cat.img,(self.game_cat.img_rect[0],
                                                self.game_cat.img_rect[1]))
            self.window.blit(self.game_score.text,(self.game_score.text_rect[0],
                                                   self.game_score.text_rect[1]))
    def action(self):
        if self.is_start ==True:
            self.game_fish.move_down()
    def event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if self.is_start == False:
                    self.is_start = True
                    print("可以开始游戏")
            if event.type == pygame.MOUSEMOTION:
                if self.is_start == True:
                    self.game_cat.move(event.pos)
    def update(self):
        pygame.display.update()

    def cat_eat_fish(self):
        flag = pygame.Rect.contains(self.game_cat.img_rect,self.game_fish.img_rect)
        if flag == True:
            self.game_fish.reset()
            self.game_score.set_text()
    def run(self):
        while True:
            self.draw()
            self.action()
            self.event()
            self.cat_eat_fish()
            self.update()


# 创建游戏入口
if __name__ == '__main__':
    dir(pygame)
    game = GameWindow()
    game.run()