import pygame


class Settings():
    """存储所有设置的类"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.name = '小火箭'
        self.bg_color = (230, 230, 230)

        # 火箭移动速度
        self.rocket_move_speed = 2

        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_limit = 5
