import pygame
from sys import exit
from PIL import Image, ImageDraw

class Sprite():
    def __init__(self, name, dir=1, res=(800,400)):
        self.name = name
        self.dir = dir
        self.res = res

    def draw(self, screen):
        surf = pygame.image.load(f"img_files/spr_{self.name}.png")
        if self.dir == 0:
            surf = pygame.transform.flip(surf, 1, 0)
        screen.blit(surf, (0,0))

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()
    sprite = Sprite(name="protag")
    font = pygame.font.SysFont('Comic Sans MS', 18)

    background = pygame.image.load('img_files/bg_placeholder.png')
    txt_box = pygame.image.load('img_files/ui_textbox.png')
    txt_surface = font.render('Lorum Ipsum', False, (255, 255, 255))

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sprite.dir==1:
                    sprite = Sprite(name="altchara", dir=0)
                else:
                    sprite = Sprite(name="protag", dir=1)

        screen.blit(background, (0,0))
        sprite.draw(screen)
        screen.blit(txt_box, (0,0))
        screen.blit(txt_surface, (30, 240))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()