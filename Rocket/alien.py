import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, my_set, screen):
        super().__init__()
        self.screen = screen
        self.my_set = my_set

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.ico')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定区域绘制外星人"""
        self.screen.blit(self.image,self.rect)
