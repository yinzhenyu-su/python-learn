import pygame
from pygame.sprite import Group
from settings import Settings
from rocket import Rocket
from alien import Alien
import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    my_set = Settings()

    screen = pygame.display.set_mode(
        (my_set.screen_width, my_set.screen_height))
    # 设置游戏名
    pygame.display.set_caption(my_set.name)
    # 创建一艘火箭
    my_rocket = Rocket(my_set, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    alien = Alien(my_set, screen)
    # 游戏主循环
    while True:
        gf.check_events(my_set, screen, my_rocket, bullets)
        my_rocket.update(my_set, screen)
        gf.update_bullets(bullets)
        gf.update_screen(my_set, screen, my_rocket, bullets, alien)


run_game()
