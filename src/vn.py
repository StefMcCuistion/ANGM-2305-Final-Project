import pygame
from sys import exit

class Sprite():
    def __init__(self, name, dir=1, res=(800,400)):
        self.name = name # name of the character protrayed in the sprite
        self.dir = dir # determines whether sprite faces left or right, 1 = right, 0 = left
        self.res = res # determines what resolution the sprite displays at

    def draw(self, screen):
        """
        Draws character sprite on screen. 

        :param screen: The 'screen' surface that other surfaces are blitted onto. 
        :type screen: Surface
        """
        surf = pygame.image.load(f"img_files/spr_{self.name}.png")
        if self.dir == 0:
            surf = pygame.transform.flip(surf, 1, 0)
        screen.blit(surf, (0,0))

def display_dialogue(screen, txt, font):
    print(f"txt={txt}") #debug
    txt = txt.split('\n')
    line1 = font.render(txt[0], False, (255, 255, 255))
    print(f"line1={line1}") #debug
    line2 = font.render(txt[1], False, (255, 255, 255))
    print(f"line2={line2}") #debug
    line3 = font.render(txt[2], False, (255, 255, 255))
    line4 = font.render(txt[3], False, (255, 255, 255))
    line5 = font.render(txt[4], False, (255, 255, 255))
    screen.blit(line1, (30, 240))
    screen.blit(line2, (30, 270))
    screen.blit(line3, (30, 300))
    screen.blit(line4, (30, 330))
    screen.blit(line5, (30, 360))


def main():
    # Initialization and setup. 

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()
    sprite = Sprite(name="protag")
    font = pygame.font.SysFont('Comic Sans MS', 18)

    background = pygame.image.load('img_files/bg_placeholder.png')
    txt_box = pygame.image.load('img_files/ui_textbox.png')

    with open('dialogue.csv') as file:
        pages = []
        for line in file:
            pages.append(line)

    # The main game loop. 
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # This will eventually progress dialogue. 
                # For now, it swaps between protagonist and alt character. 
                if sprite.dir==1:
                    sprite = Sprite(name="altchara", dir=0)
                else:
                    sprite = Sprite(name="protag", dir=1)

        #TODO: Add main menu
        #TODO: Add external text document to grab dialogue from
        #TODO: Make code display arbitrary text with arbitrary number of 'pages'
        #TODO: Add settings menu
        #TODO: Add audio
        #TODO: Add end screen

        screen.blit(background, (0,0))
        sprite.draw(screen)
        screen.blit(txt_box, (0,0))
        print(f"The first item of the list 'pages' is {pages[0]}") #debug
        display_dialogue(screen, pages[0], font)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()