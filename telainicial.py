class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


import pygame, sys, sologame


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Humberpong")

STARTBACKGROUND = pygame.image.load("assets/image/background.png").convert()
INSTRUCTIONBACKGROUND = pygame.image.load("assets/image/buttonsbackground.png").convert()
KEYS_ARROWS = pygame.image.load("assets/image/teclas_setas.png")
KEYS_WASD = pygame.image.load("assets/image/teclas_WASD.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def SOLO():
    while True:
        SOLO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        SOLO_TEXT = get_font(20).render("Use as setinhas para movimentar seu jogador!", True, "White")
        SOLO_RECT = SOLO_TEXT.get_rect(center=(650, 100))
        SOLO_BACKGROUND = pygame.transform.scale(INSTRUCTIONBACKGROUND, (1280, 720))
        SCREEN.blit(SOLO_BACKGROUND, (0, 0))
        SCREEN.blit(SOLO_TEXT, SOLO_RECT)
        SCREEN.blit(KEYS_ARROWS, (350, 120))
        
        SOLO_START = Button(image=None, pos=(975, 600), 
                            text_input="START", font=get_font(75), base_color="White", hovering_color="Green")
        SOLO_BACK = Button(image=None, pos=(350, 600), 
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
                    

        pygame.display.update()
    
def PVP():
    while True:
        PVP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        
        PVP_TEXT1 = get_font(20).render("Player 1 ", True, "White")
        PVP_TEXT2 = get_font(20).render("Player 2 ", True, "White")
        PVP_RECT1 = PVP_TEXT1.get_rect(center=(300, 100))
        PVP_RECT2 = PVP_TEXT1.get_rect(center=(975, 100))
        PVP_BACKGROUND = pygame.transform.scale(INSTRUCTIONBACKGROUND, (1280, 720))
        SCREEN.blit(PVP_BACKGROUND, (0, 0))
        SCREEN.blit(PVP_TEXT1, PVP_RECT1)
        SCREEN.blit(PVP_TEXT2, PVP_RECT2)
        SCREEN.blit(KEYS_WASD, (20, 70))
        SCREEN.blit(KEYS_ARROWS, (680, 120))

        PVP_BACK = Button(image=None, pos=(640, 600), 
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
        
        BG = pygame.transform.scale(STARTBACKGROUND, (1280, 720))
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("HUMBERPONG", True, "Purple")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        SOLO_BUTTON = Button(image=pygame.image.load("assets/image/Play Rect.png"), pos=(640, 250), 
                            text_input="SOLO", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PVP_BUTTON = Button(image=pygame.image.load("assets/image/Options Rect.png"), pos=(640, 400), 
                            text_input="1V1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/image/Quit Rect.png"), pos=(640, 550), 
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