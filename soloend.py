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

winner_sound = pygame.mixer.Sound("assets/snd/winner.mp3")
lose_sound = pygame.mixer.Sound("assets/snd/lose.mp3")

def WINNER():
    while True: 
        
        pygame.mixer.Sound.play(winner_sound)

        WINNER_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        WINNER_TEXT = get_font(20).render("PARABÉNS, VOCÊ GANHOU!!!", True, "White")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(750, 100))
        WINNER_BACKGROUND = pygame.transform.scale(BACKGROUND, (1550, 810))
        WINNER_IMAGE = pygame.transform.scale(WIN_IMAGE, (1600/3, 1210/3))
        screen.blit(WINNER_BACKGROUND, (0, 0))
        screen.blit(WINNER_TEXT, WINNER_RECT)
        screen.blit(WINNER_IMAGE, (525, 200))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        
        pygame.display.update()   

def LOSE():
    while True:
        
        pygame.mixer.Sound.play(lose_sound)
        
        LOSE_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        LOSE_TEXT = get_font(20).render("Você perdeu, tente novamente! ;-;", True, "White")
        LOSE_RECT = LOSE_TEXT.get_rect(center=(750, 100))
        LOSE_BACKGROUND = pygame.transform.scale(BACKGROUND, (1550, 810))
        screen.blit(LOSE_BACKGROUND, (0, 0))
        screen.blit(LOSE_TEXT, LOSE_RECT)
        screen.blit(LOSE_IMAGE, (575, 200))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        
        pygame.display.update()   