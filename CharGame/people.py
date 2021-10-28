import pygame
from pygame import *


class People():
    def __init__(self, life, age, energy, useful, words=""):
        super(People, self).__init__()
        self.life = life
        self.age = age
        self.energy = energy
        self.useful = useful
        self.words = words
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.y -= 5
            print(self.rect.y)
        if pressed_keys[K_DOWN]:
            self.rect.y += 5
        if pressed_keys[K_LEFT]:
            self.rect.x -= 5
        if pressed_keys[K_RIGHT]:
            self.rect.x += 5
    def draw(self,screen):
        screen.blit(self.surf, (self.rect.x, self.rect.y))
    def grow(self, energy):
        self.age += 1
        self.energy += energy

    def say(self, words):
        self.words = words

    def die(self):
        with open(file="history.txt", mode="w", encoding="utf-8") as file:
            file.write(chr(self.age))
