from pygame.locals import *
from people import People


def run_game():
    running = True
    # pygame.init()
    p = People(100, 0, 0, True)
    while running:

        # screen = pygame.display.set_mode((800, 600))
        # # 退出
        # p = People(100, 0, 0, True)
        # surf = pygame.Surface((50, 50))
        # surf.fill((255, 255, 255))
        # rect = surf.get_rect()

        # for event in pygame.event.get():
        #     if event.type == KEYDOWN:
        #         if event.key == K_ESCAPE:
        #             running = False
        #     elif event.type == QUIT:
        #         running = False
        # pressed_keys = pygame.key.get_pressed()
        # p.update(pressed_keys)
        # p.draw(screen)
        # pygame.display.flip()
        
        if p.useful:
            print("Status:useful");
            


if __name__ == '__main__':
    run_game()
