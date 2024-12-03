import pygame
from sys import exit

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
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()
    sprite = Sprite(name="protag")

    background = pygame.image.load('img_files/bg_placeholder.png')
    text_box = pygame.image.load('img_files/ui_textbox.png')

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
        screen.blit(text_box, (0,0))
        sprite.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()