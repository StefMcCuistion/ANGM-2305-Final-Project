import pygame
from sys import exit

class Sprite():
    def __init__(self, name, dir, res):
        self.name = name
        self.dir = dir
        self.res = res

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Visual Novel')
clock = pygame.time.Clock()

test_surface = pygame.image.load('img_files/bg.png')

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0,0))

    pygame.display.update()
    clock.tick(60)