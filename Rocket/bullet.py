import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """模拟子弹的类"""

    def __init__(self, my_set, screen, my_rocket):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(
            0, 0, my_set.bullet_width, my_set.bullet_height)
        self.rect.centerx = my_rocket.rect.centerx
        self.rect.top = my_rocket.rect.top

        self.y = float(self.rect.y)
        self.color = my_set.bullet_color
        self.speed = my_set.bullet_speed_factor

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
