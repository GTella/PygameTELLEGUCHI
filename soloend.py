import pygame, sys
from other import Button, get_font

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
SCREEN_WIDTH = 1550
SCREEN_HEIGHT = 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HUMBERPONG')

BACKGROUND = pygame.image.load("assets/image/background.png").convert()
WIN_IMAGE = pygame.image.load("assets/image/winner.png")
LOSE_IMAGE = pygame.image.load("assets/image/game_over.png")

def WINNER():
    while True:
        WINNER_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        WINNER_TEXT = get_font(20).render("Use as setinhas para movimentar seu jogador!", True, "White")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(750, 100))
        WINNER_BACKGROUND = pygame.transform.scale(BACKGROUND, (1550, 810))
        screen.blit(WINNER_BACKGROUND, (0, 0))
        screen.blit(WINNER_TEXT, WINNER_RECT)
        screen.blit(WIN_IMAGE, (450, 150))
        
        WINNER_RESTART = Button(image=None, pos=(1075, 700), 
                            text_input="RESTART", font=get_font(75), base_color="White", hovering_color="Green")
        WINNER_MENU = Button(image=None, pos=(450, 700), 
                            text_input="MENU", font=get_font(75), base_color="White", hovering_color="Red")

        WINNER_MENU.changeColor(WINNER_MOUSE_POS)
        WINNER_MENU.update(screen)
        WINNER_RESTART.changeColor(WINNER_MOUSE_POS)
        WINNER_RESTART.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WINNER_MENU.checkForInput(WINNER_MOUSE_POS):
                    print ('YEY')
        
        pygame.display.update()   

def LOSE():
    while True:
        LOSE_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        LOSE_TEXT = get_font(20).render("Use as setinhas para movimentar seu jogador!", True, "White")
        LOSE_RECT = LOSE_TEXT.get_rect(center=(750, 100))
        LOSE_BACKGROUND = pygame.transform.scale(BACKGROUND, (1550, 810))
        screen.blit(LOSE_BACKGROUND, (0, 0))
        screen.blit(LOSE_TEXT, LOSE_RECT)
        screen.blit(LOSE_IMAGE, (450, 150))
        
        LOSE_RESTART = Button(image=None, pos=(1075, 700), 
                            text_input="RESTART", font=get_font(75), base_color="White", hovering_color="Green")
        LOSE_MENU = Button(image=None, pos=(450, 700), 
                            text_input="MENU", font=get_font(75), base_color="White", hovering_color="Red")

        LOSE_MENU.changeColor(LOSE_MOUSE_POS)
        LOSE_MENU.update(screen)
        LOSE_RESTART.changeColor(LOSE_MOUSE_POS)
        LOSE_RESTART.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOSE_MENU.checkForInput(LOSE_MOUSE_POS):
                    print('YEY')
        
        pygame.display.update()   