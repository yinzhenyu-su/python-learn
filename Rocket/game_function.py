import sys
import pygame
from bullet import Bullet


def fire_bullet(my_set, screen, my_rocket, bullets):
    if len(bullets) < my_set.bullet_limit:
        new_bullet = Bullet(my_set, screen, my_rocket)
        bullets.add(new_bullet)


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


# 按下按键
def check_key_down(event, my_set, screen, my_rocket, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_LEFT:
        my_rocket.moving_left = True
    if event.key == pygame.K_RIGHT:
        my_rocket.moving_right = True
    if event.key == pygame.K_UP:
        my_rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        my_rocket.moving_down = True
    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
        fire_bullet(my_set, screen, my_rocket, bullets)


# 松开按键
def check_key_up(event, my_rocket):
    if event.key == pygame.K_LEFT:
        my_rocket.moving_left = False
    if event.key == pygame.K_RIGHT:
        my_rocket.moving_right = False
    if event.key == pygame.K_UP:
        my_rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        my_rocket.moving_down = False


def check_events(my_set, screen, my_rocket, bullets):
    """检查键盘输入"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, my_set, screen, my_rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up(event, my_rocket)


def update_screen(my_set, screen, my_rocket, bullets, alien):
    """更新屏幕"""
    # 背景设置
    screen.fill(my_set.bg_color)
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 在屏幕中画出火箭
    my_rocket.blitme()
    alien.blitme()
    pygame.display.flip()
