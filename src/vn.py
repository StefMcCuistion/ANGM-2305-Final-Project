import pygame
from sys import exit

class Sprite():
    def __init__(self, name="protag", dir=1, res=(800,400)):
        self.name = name # name of the character protrayed in the sprite
        self.dir = dir # determines whether sprite faces left or right, 1 = right, 0 = left
        self.res = res # determines what resolution the sprite displays at

    def draw(self, screen, res):
        """
        Draws character sprite on screen. 

        :param screen: The 'screen' surface that other surfaces are blitted onto. 
        :type screen: Surface

        :return: None. 
        :rtype: None. 
        """
        surf = pygame.image.load(f"img_files/spr_{self.name}_{res[0]}x{res[1]}.png")
        if self.dir == 0:
            surf = pygame.transform.flip(surf, 1, 0)
        screen.blit(surf, (0,0))

def display_dialogue(screen, txt, font, res):
    """
    Displays text in dialogue box. 

    :param txt: The text that will be displayed. 
    :type txt: str

    :param font: The font that the text will be displayed in. 
    :type font: font

    :return: None. 
    :rtype: None. 
    """
    txt = txt.split('\\n')
    line1 = font.render(txt[0], False, (255, 255, 255))
    line2 = font.render(txt[1], False, (255, 255, 255))
    line3 = font.render(txt[2], False, (255, 255, 255))
    line4 = font.render(txt[3], False, (255, 255, 255))
    line5 = font.render(txt[4], False, (255, 255, 255))
    screen.blit(line1, (0.0375*res[0], 0.6*res[1]))
    screen.blit(line2, (0.0375*res[0], 0.675*res[1]))
    screen.blit(line3, (0.0375*res[0], 0.75*res[1]))
    screen.blit(line4, (0.0375*res[0], 0.825*res[1]))
    screen.blit(line5, (0.0375*res[0], 0.9*res[1]))

def update_page(page, sprite):
    print(f"The current page is {page}!") #debug
    if sprite.dir==1:
        sprite = Sprite(dir=0)
    else:
        sprite = Sprite(name="altchara", dir=1)
    return sprite

def update_background(background, time, res):
    background = pygame.image.load(f'img_files/bg_{time}_{res[0]}x{res[1]}.png')
    return background

def update_txtbox(txt_box, res):
    txt_box = pygame.image.load(f'img_files/ui_textbox_{res[0]}x{res[1]}.png')
    return txt_box

def play():
    res = (800, 400)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()
    sprite = Sprite(name="altchara")
    font = pygame.font.SysFont('Comic Sans MS', int(0.0225*res[0]))
    page = 1
    time = 'night'
    print(f"The current page is {page}!") #debug

    background = pygame.image.load(f'img_files/bg_{time}_{res[0]}x{res[1]}.png')
    txt_box = pygame.image.load(f'img_files/ui_textbox_{res[0]}x{res[1]}.png')


    with open('dialogue.csv') as file:
        dialogue_pages = []
        scene_pages = []
        for line in file:
            scene, dialogue = line.rstrip().split('*')
            dialogue_pages.append(dialogue)
            scene_pages.append(scene)


    # The main game loop. 
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pagecount = len(dialogue_pages)
                if page < pagecount:
                    page += 1
                    sprite = update_page(page, sprite)
                    background = update_background(background, time, res)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if res == (800, 400):
                        res = (1040, 520)
                    elif res == (1040, 520):
                        res = (800, 400)
                    print(f"res={res}")
                    screen = pygame.display.set_mode(res)
                    background = update_background(background, time, res)
                    txt_box = update_txtbox(txt_box, res)
        screen.blit(background, (0,0))
        sprite.draw(screen, res)
        screen.blit(txt_box, (0,0))
        display_dialogue(screen, dialogue_pages[page-1], font, res)

        pygame.display.update()
        clock.tick(60)

def main_menu():
    res = (800, 400)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play()


def main():
    # Initialization and setup. 
    pygame.init()
    pygame.font.init()

        #TODO: Add main menu
        #TODO: Add unique sprites for each page
        #TODO: Add settings menu
        #TODO: Add audio
        #TODO: Add end screen

    main_menu()


if __name__ == "__main__":
    main()