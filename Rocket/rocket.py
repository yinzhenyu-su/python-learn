import pygame


class Rocket():
    def __init__(self, my_set, screen):
        """初始化火箭并设置其初始位置"""
        self.screen = screen

        # 加载火箭图像并获取其外接矩形
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        # 获取屏幕矩形
        self.screen_rect = self.screen.get_rect()

        # 将每艘新火箭放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动火箭的开关
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)

    def update(self, my_set, screen):
        """更新火箭在屏幕中的位置"""
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= my_set.rocket_move_speed
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.rect.centerx += my_set.rocket_move_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.bottom -= my_set.rocket_move_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.bottom += my_set.rocket_move_speed
