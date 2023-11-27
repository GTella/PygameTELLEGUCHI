
import pygame, sys
from solo import sologame
from other import Button, get_font
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()


SCREEN = pygame.display.set_mode((1550, 810))
pygame.display.set_caption("Humberpong")

STARTBACKGROUND = pygame.image.load("assets/image/background.png").convert()
INSTRUCTIONBACKGROUND = pygame.image.load("assets/image/buttonsbackground.png").convert()
KEYS_ARROWS = pygame.image.load("assets/image/teclas_setas.png")
KEYS_WASD = pygame.image.load("assets/image/teclas_WASD.png")

menu_sound = pygame.mixer.Sound("assets/snd/menu.mp3")

def SOLO():
    while True:
        SOLO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        SOLO_TEXT = get_font(20).render("Use as setinhas para movimentar seu jogador!", True, "White")
        SOLO_RECT = SOLO_TEXT.get_rect(center=(750, 100))
        SOLO_BACKGROUND = pygame.transform.scale(INSTRUCTIONBACKGROUND, (1550, 810))
        SCREEN.blit(SOLO_BACKGROUND, (0, 0))
        SCREEN.blit(SOLO_TEXT, SOLO_RECT)
        SCREEN.blit(KEYS_ARROWS, (450, 150))
        
        SOLO_START = Button(image=None, pos=(1075, 700), 
                            text_input="START", font=get_font(75), base_color="White", hovering_color="Green")
        SOLO_BACK = Button(image=None, pos=(450, 700), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        SOLO_BACK.changeColor(SOLO_MOUSE_POS)
        SOLO_BACK.update(SCREEN)
        SOLO_START.changeColor(SOLO_MOUSE_POS)
        SOLO_START.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SOLO_BACK.checkForInput(SOLO_MOUSE_POS):
                    main_menu()
                if SOLO_START.checkForInput(SOLO_MOUSE_POS):
                    sologame()
        pygame.display.update()
    
def PVP():
    while True:
        PVP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        
        PVP_TEXT1 = get_font(20).render("Player 1 ", True, "White")
        PVP_TEXT2 = get_font(20).render("Player 2 ", True, "White")
        PVP_RECT1 = PVP_TEXT1.get_rect(center=(400, 130))
        PVP_RECT2 = PVP_TEXT1.get_rect(center=(1075, 130))
        PVP_BACKGROUND = pygame.transform.scale(INSTRUCTIONBACKGROUND, (1550, 810))
        SCREEN.blit(PVP_BACKGROUND, (0, 0))
        SCREEN.blit(PVP_TEXT1, PVP_RECT1)
        SCREEN.blit(PVP_TEXT2, PVP_RECT2)
        SCREEN.blit(KEYS_WASD, (120, 100))
        SCREEN.blit(KEYS_ARROWS, (780, 150))

        PVP_BACK = Button(image=None, pos=(740, 700), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PVP_BACK.changeColor(PVP_MOUSE_POS)
        PVP_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PVP_BACK.checkForInput(PVP_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        
        pygame.mixer.Sound.play(menu_sound)
        
        BG = pygame.transform.scale(STARTBACKGROUND, (1550, 810))
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("HUMBERPONG", True, "Purple")
        MENU_RECT = MENU_TEXT.get_rect(center=(740, 150))

        SOLO_BUTTON = Button(image=pygame.image.load("assets/image/Play Rect.png"), pos=(740, 350), 
                            text_input="SOLO", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PVP_BUTTON = Button(image=pygame.image.load("assets/image/Options Rect.png"), pos=(740, 500), 
                            text_input="1V1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/image/Quit Rect.png"), pos=(740, 650), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [SOLO_BUTTON, PVP_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SOLO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    SOLO()
                if PVP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    PVP()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()