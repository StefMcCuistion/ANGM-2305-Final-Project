import pygame
from pygame import mixer
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

class Button():
    def __init__(self, name, img, x, y, binary = 0, on_or_off = "on", 
                resolution = (1040, 520)):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.binary = binary
        self.on_or_off = on_or_off
        self.res = resolution
        self.rect = self.img.get_rect(center=(self.x, self.y))
        self.button_sound = pygame.mixer.Sound("audio_files/sfx_button.mp3")

    def update(self, screen):
        screen.blit(self.img, self.rect)

    def check_for_input(self, pos, sfx):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            if sfx == 1:
                    self.button_sound.play()
            return 1
        else:
            return 0

    def change_appearance(self, pos, res):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            if self.binary:
                self.img = pygame.image.load(
                    f"img_files/ui_{self.name}_{self.on_or_off}_selected_{res[0]}x{res[1]}.png")
            else:
                self.img = pygame.image.load(
                    f"img_files/ui_{self.name}_selected_{res[0]}x{res[1]}.png")
        else:
            if self.binary:
                self.img = pygame.image.load(
                    f"img_files/ui_{self.name}_{self.on_or_off}_unselected_{res[0]}x{res[1]}.png")
            else:
                self.img = pygame.image.load(
                    f"img_files/ui_{self.name}_unselected_{res[0]}x{res[1]}.png")


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

def play(res, music, sfx, game_res):
    screen = pygame.display.set_mode(game_res)
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()
    sprite = Sprite(name="altchara")
    font = pygame.font.SysFont('Comic Sans MS', int(0.0225*res[0]))
    page = 1
    time = 'day'
    res = game_res

    background = pygame.image.load(f'img_files/bg_{time}_{res[0]}x{res[1]}.png')
    txt_box = pygame.image.load(f'img_files/ui_textbox_{res[0]}x{res[1]}.png')
    pageturn_sfx = pygame.mixer.Sound("audio_files/sfx_pageturn.mp3")


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
                    if sfx:
                        pageturn_sfx.play()
                    page += 1
                    sprite = update_page(page, sprite)
                    background = update_background(background, time, res)
                else:
                    res = (1040, 520)
                    main_menu(res, music, sfx, game_res)
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

def main_menu(res, music, sfx, game_res):
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()

    start_button_surface = pygame.image.load(
        f"img_files/ui_start_unselected_{res[0]}x{res[1]}.png")
    options_button_surface = pygame.image.load(
        f"img_files/ui_options_unselected_{res[0]}x{res[1]}.png")
    quit_button_surface = pygame.image.load(
        f"img_files/ui_quit_unselected_{res[0]}x{res[1]}.png")

    start_button = Button(name="start", img=start_button_surface,
                           x=(res[0]*0.5), y=(res[1]*0.4), resolution=(1040,520))
    options_button = Button(name="options", img=options_button_surface,
                             x=(res[0]*0.5), y=(res[1]*0.6), resolution=(1040,520))
    quit_button = Button(name="quit", img=quit_button_surface,
                          x=(res[0]*0.5), y=(res[1]*0.8), resolution=(1040,520))

    screen.fill('black')
    bg_img = pygame.image.load(f"img_files/ui_main_menu_{res[0]}x{res[1]}.png")
    screen.blit(bg_img, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                progress = start_button.check_for_input(pygame.mouse.get_pos(), sfx)
                if progress:
                    play(res, music, sfx, game_res)
                close = quit_button.check_for_input(pygame.mouse.get_pos(), sfx)
                if close:
                    pygame.quit()
                    exit()
                options = options_button.check_for_input(pygame.mouse.get_pos(), sfx)
                if options:
                    settings_menu(res, music, sfx, game_res)
                    break
                    
        
        start_button.update(screen)
        options_button.update(screen)
        quit_button.update(screen)
        start_button.change_appearance(pygame.mouse.get_pos(), res)
        options_button.change_appearance(pygame.mouse.get_pos(), res)
        quit_button.change_appearance(pygame.mouse.get_pos(), res)
        
        pygame.display.update()
        clock.tick(60)

def settings_menu(res, music, sfx, game_res):
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('Visual Novel')
    clock = pygame.time.Clock()

    button_sound = pygame.mixer.Sound("audio_files/sfx_button.mp3")

    if sfx:
        sfx_button_label = "on"
    else:
        sfx_button_label = "off"

    if music:
        music_button_label = "on"
    else:
        music_button_label = "off"

    if game_res == (1040, 520):
        game_res_label = "on"
    else:
        game_res_label = "off"

    return_button_surface = pygame.image.load(
        f"img_files/ui_return_unselected_{res[0]}x{res[1]}.png")
    music_button_surface = pygame.image.load(
        f"img_files/ui_music_{music_button_label}_unselected_{res[0]}x{res[1]}.png")
    sfx_button_surface = pygame.image.load(
        f"img_files/ui_sfx_{sfx_button_label}_unselected_{res[0]}x{res[1]}.png")
    res_button_surface = pygame.image.load(
        f"img_files/ui_resbutton_{game_res_label}_unselected_{res[0]}x{res[1]}.png")

    return_button = Button(name="return", img=return_button_surface, x=(res[0]*0.5), y=(res[1]*0.8),
                            resolution=(1040,520))
    music_button = Button(name="music", img=music_button_surface, x=(res[0]*0.7), y=(res[1]*0.28),
                          binary = 1, on_or_off=music_button_label, resolution=(1040,520))
    sfx_button = Button(name="sfx", img=sfx_button_surface, x=(res[0]*0.7), y=(res[1]*0.43),
                        binary = 1, on_or_off=sfx_button_label, resolution=(1040,520))
    res_button = Button(name="resbutton", img=res_button_surface, x=(res[0]*0.8), y=(res[1]*0.57),
                        binary = 1, on_or_off = game_res_label, resolution=(1040,520))

    screen.fill('black')
    bg = pygame.image.load(f"img_files/ui_settings_{res[0]}x{res[1]}.png")
    screen.blit(bg, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                back = return_button.check_for_input(pygame.mouse.get_pos(), sfx)
                music_toggle = music_button.check_for_input(pygame.mouse.get_pos(), sfx)
                sfx_toggle = sfx_button.check_for_input(pygame.mouse.get_pos(), sfx)
                res_toggle = res_button.check_for_input(pygame.mouse.get_pos(), sfx)
                if back:
                    main_menu(res, music, sfx, game_res)
                    break
                if music_toggle:
                    if music_button.on_or_off == "on":
                        music_button.on_or_off = "off"
                    else:
                        music_button.on_or_off = "on"
                    if music == 1:
                        music = 0
                        mixer.music.stop()
                    else:
                        music = 1
                        mixer.music.play()
                if sfx_toggle:
                    if sfx_button.on_or_off == "on":
                        sfx_button.on_or_off = "off"
                    else:
                        sfx_button.on_or_off = "on"
                        button_sound.play()
                    if sfx == 1:
                        sfx = 0
                    else:
                        sfx = 1
                if res_toggle:
                    if res_button.on_or_off == "on":
                        res_button.on_or_off = "off"
                        game_res = (800, 400)
                    else:
                        res_button.on_or_off = "on"
                        game_res = (1040, 520)
                
        
        return_button.update(screen)
        music_button.update(screen)
        sfx_button.update(screen)
        res_button.update(screen)
        return_button.change_appearance(pygame.mouse.get_pos(), res)
        music_button.change_appearance(pygame.mouse.get_pos(), res)
        sfx_button.change_appearance(pygame.mouse.get_pos(), res)
        res_button.change_appearance(pygame.mouse.get_pos(), res)
        
        pygame.display.update()
        clock.tick(60)

def main():
    # Initialization and setup. 
    pygame.init()
    pygame.font.init()
    res = (1040, 520)
    music = 1
    sfx = 1
    game_res = res

    mixer.music.load("audio_files/music_menu.mp3")
    mixer.music.play(-1)

    main_menu(res, music, sfx, game_res)


if __name__ == "__main__":
    main()