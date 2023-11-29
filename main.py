import pygame, sys, random
from other import Button, get_font

def WINNER():
    BACKGROUND = pygame.image.load("assets/image/background.png").convert()
    WIN_IMAGE = pygame.image.load("assets/image/winner.png")
    winner_sound = pygame.mixer.Sound("assets/snd/winner.mp3")
   
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
        

        WIN_RESTART = Button(image=None, pos=(1075, 700), 
                            text_input="RESTART", font=get_font(75), base_color="White", hovering_color="Green")
        WIN_MENU = Button(image=None, pos=(450, 700), 
                            text_input="MENU", font=get_font(75), base_color="White", hovering_color="Red")

        WIN_MENU.changeColor(WINNER_MOUSE_POS)
        WIN_MENU.update(screen)
        WIN_RESTART.changeColor(WINNER_MOUSE_POS)
        WIN_RESTART.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_RESTART.checkForInput(WINNER_MOUSE_POS):
                    pygame.mixer.Sound.stop(winner_sound)
                    sologame()
                if WIN_MENU.checkForInput(WINNER_MOUSE_POS):
                    pygame.mixer.Sound.stop(winner_sound)
                    main_menu()
            
            pygame.display.update()   

def LOSE():
    BACKGROUND = pygame.image.load("assets/image/background.png").convert()
    LOSE_IMAGE = pygame.image.load("assets/image/game_over.png")
    lose_sound = pygame.mixer.Sound("assets/snd/lose.mp3")
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
                if LOSE_RESTART.checkForInput(LOSE_MOUSE_POS):
                    pygame.mixer.Sound.stop(lose_sound)
                    sologame()
                if LOSE_MENU.checkForInput(LOSE_MOUSE_POS):
                    pygame.mixer.Sound.stop(lose_sound)
                    main_menu()
            
            pygame.display.update()





def pvpgame():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    def ball_animation():
        global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
        ball.x += ball_speed_x
        ball.y += ball_speed_y
    
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            pygame.mixer.Sound.play(pong_sound)
            ball_speed_y *= -1
        
        if ball.left <= 0:
            pygame.mixer.Sound.play(score_sound)
            player_score += 1
            score_time = pygame.time.get_ticks()
        
        if ball.right >= SCREEN_WIDTH:
            pygame.mixer.Sound.play(score_sound)
            opponent_score += 1
            score_time = pygame.time.get_ticks()
        
        if ball.colliderect(player) and ball_speed_x > 0:
            pygame.mixer.Sound.play(pong_sound)
            if abs(ball.right - player.left) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - player.bottom) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1

        if ball.colliderect(opponent) and ball_speed_x < 0:
            pygame.mixer.Sound.play(pong_sound)
            if abs(ball.left - opponent.right) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1

    def player_animation():
        player.y += player_speed
    
        if player.top <= 0:
            player.top = 0
        if player.bottom >= SCREEN_HEIGHT:
            player.bottom = SCREEN_HEIGHT
        
    def opponent_animation():
        opponent.y += opponent_speed
    
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= SCREEN_HEIGHT:
            opponent.bottom = SCREEN_HEIGHT
        
    
        
    def ball_restart():
        global ball_speed_x, ball_speed_y, score_time
    
        current_time = pygame.time.get_ticks()
        ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
        if current_time - score_time < 700:
            number_three = game_font.render('3', False, light_grey)
            screen.blit(number_three, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))
        
        if 700 < current_time - score_time < 1400:
            number_number = game_font.render('2', False, light_grey)
            screen.blit(number_number, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))   
        
        if 1400 < current_time - score_time < 2100:
            number_one = game_font.render('1', False, light_grey)
            screen.blit(number_one, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))  
        
        if current_time - score_time < 2100:
            ball_speed_x, ball_speed_y = 0,0
        
        else:
            ball_speed_y = 9 * random.choice((1, -1))
            ball_speed_x = 9 * random.choice((1, -1))
            score_time = None
            
    def PVPWIN():
        
        WIN_IMAGE = pygame.image.load("assets/image/winner.png")
        BACKGROUND = pygame.image.load("assets/image/background.png").convert()
        winner_sound = pygame.mixer.Sound("assets/snd/winner.mp3")
        if opponent_score == 3:
            x = 'Player 1'
        if player_score == 3:
            x = 'Player 2'

        while True: 
            
            WINNER_MOUSE_POS = pygame.mouse.get_pos()
            pygame.mixer.Sound.play(winner_sound)
            if opponent_score == 3:
                x = 'Player 1'
            if player_score == 3:
                x = 'Player 2'
            screen.fill("black")
            WINNER_TEXT = get_font(20).render("PARABÉNS, {0} GANHOU!!!".format(x), True, "White")
            WINNER_RECT = WINNER_TEXT.get_rect(center=(750, 100))
            WINNER_BACKGROUND = pygame.transform.scale(BACKGROUND, (1550, 810))
            WINNER_IMAGE = pygame.transform.scale(WIN_IMAGE, (1600/3, 1210/3))
            screen.blit(WINNER_BACKGROUND, (0, 0))
            screen.blit(WINNER_TEXT, WINNER_RECT)
            screen.blit(WINNER_IMAGE, (525, 200))
            
            PVP_RESTART = Button(image=None, pos=(1075, 700), 
                            text_input="RESSTART", font=get_font(75), base_color="White", hovering_color="Green")
            PVP_MENU = Button(image=None, pos=(450, 700), 
                            text_input="MENU", font=get_font(75), base_color="White", hovering_color="Red")

            PVP_MENU.changeColor(WINNER_MOUSE_POS)
            PVP_MENU.update(screen)
            PVP_RESTART.changeColor(WINNER_MOUSE_POS)
            PVP_RESTART.update(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PVP_RESTART.checkForInput(WINNER_MOUSE_POS):
                        pygame.mixer.Sound.stop(winner_sound)
                        pvpgame()
                    if PVP_MENU.checkForInput(WINNER_MOUSE_POS):
                        pygame.mixer.Sound.stop(winner_sound)
                        main_menu()
            
            pygame.display.update()
            

    # ===== General Setup ===== #
    pygame.mixer.pre_init(44100,-16,2,220)
    pygame.init()
    clock = pygame.time.Clock()

    # ===== Setup The Main Window ===== #
    SCREEN_WIDTH = 1550
    SCREEN_HEIGHT = 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('HUMBERPONG')

    # ===== Game Rectangles ===== #

    #ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 - 15, 30, 30)
    # Carregar a imagem (sprite)
    humberto_image = pygame.image.load("assets/image/humberto.png")
    humberto_image = pygame.transform.scale(humberto_image, (30, 30))
    humberto_rect = humberto_image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    ball = humberto_rect

    player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 70, 10, 140)
    opponent = pygame.Rect(10, SCREEN_HEIGHT/2 - 70, 10, 140)

    bg_color = pygame.Color('grey12')
    light_grey = (200, 200, 200)

    ball_speed_x = 11 * random.choice((1, -1))
    ball_speed_y = 11 * random.choice((1, -1))
    player_speed = 0
    opponent_speed = 0

    # ===== Text Variable ===== #
    player_score = 0
    opponent_score = 0
    game_font = pygame.font.Font('assets/font/font.ttf', 32)

    # ========= Sounds ======== #
    pong_sound = pygame.mixer.Sound("assets/snd/pong.mp3")
    score_sound = pygame.mixer.Sound("assets/snd/score.mp3")

    # ===== Images ===== #
    GAMEBACKGROUND = pygame.image.load("assets/image/background.png").convert()
    WIN_IMAGE = pygame.image.load("assets/image/winner.png")

    # ===== Score Timer ===== #
    score_time = True

    while True:
        # ===== Handling Input ===== #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 6
                if event.key == pygame.K_UP:
                    player_speed -= 6
                if event.key == pygame.K_s:
                    opponent_speed += 6
                if event.key == pygame.K_w:
                    opponent_speed -= 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 6
                if event.key == pygame.K_UP:
                    player_speed += 6
                if event.key == pygame.K_s:
                    opponent_speed -= 6
                if event.key == pygame.K_w:
                    opponent_speed += 6
        # ===== Game Logic ===== #
        ball_animation()
        player_animation()
        opponent_animation()
        
        # ===== Visuals ===== #
        screen.fill(bg_color)
        SOLO_BACKGROUND = pygame.transform.scale(GAMEBACKGROUND, (1550, 810))
        screen.blit(SOLO_BACKGROUND, (0, 0))
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    
        if player_score == 3 or opponent_score == 3:
            PVPWIN()
        if score_time:
            ball_restart()

        screen.blit(humberto_image, humberto_rect)
        
        player_text = game_font.render(f'{player_score}', False, light_grey)
        screen.blit(player_text, (850, 425))
    
        opponent_text = game_font.render(f'{opponent_score}', False, light_grey)
        screen.blit(opponent_text, (675, 425))
    
        
        # ===== Update The Window ===== #
        pygame.display.flip()
        clock.tick(60)





def sologame():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    def ball_animation():
        global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
        ball.x += ball_speed_x
        ball.y += ball_speed_y
    
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            pygame.mixer.Sound.play(pong_sound)
            ball_speed_y *= -1
        
        if ball.left <= 0:
            pygame.mixer.Sound.play(score_sound)
            player_score += 1
            score_time = pygame.time.get_ticks()
        
        if ball.right >= SCREEN_WIDTH:
            pygame.mixer.Sound.play(score_sound)
            opponent_score += 1
            score_time = pygame.time.get_ticks()
        
        if ball.colliderect(player) and ball_speed_x > 0:
            pygame.mixer.Sound.play(pong_sound)
            if abs(ball.right - player.left) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - player.bottom) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1

        if ball.colliderect(opponent) and ball_speed_x < 0:
            pygame.mixer.Sound.play(pong_sound)
            if abs(ball.left - opponent.right) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1

    def player_animation():
        player.y += player_speed
    
        if player.top <= 0:
            player.top = 0
        if player.bottom >= SCREEN_HEIGHT:
            player.bottom = SCREEN_HEIGHT
        
    def opponent_ai():
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.bottom > ball.y:
            opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= SCREEN_HEIGHT:
            opponent.bottom = SCREEN_HEIGHT
        
    
        
    def ball_restart():
        global ball_speed_x, ball_speed_y, score_time
    
        current_time = pygame.time.get_ticks()
        ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
        if current_time - score_time < 700:
            number_three = game_font.render('3', False, light_grey)
            screen.blit(number_three, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))
        
        if 700 < current_time - score_time < 1400:
            number_number = game_font.render('2', False, light_grey)
            screen.blit(number_number, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))   
        
        if 1400 < current_time - score_time < 2100:
            number_one = game_font.render('1', False, light_grey)
            screen.blit(number_one, (SCREEN_WIDTH/2 - 10, SCREEN_HEIGHT/2 + 20))  
        
        if current_time - score_time < 2100:
            ball_speed_x, ball_speed_y = 0,0
        
        else:
            ball_speed_y = 9 * random.choice((1, -1))
            ball_speed_x = 9 * random.choice((1, -1))
            score_time = None
    

    # ===== General Setup ===== #
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    clock = pygame.time.Clock()

    # ===== Setup The Main Window ===== #
    SCREEN_WIDTH = 1550
    SCREEN_HEIGHT = 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('HUMBERPONG')

    # ===== Game Rectangles ===== #
    #ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 - 15, 30, 30)
    # Carregar a imagem (sprite)
    humberto_image = pygame.image.load("assets/image/humberto.png")
    humberto_image = pygame.transform.scale(humberto_image, (30, 30))
    humberto_rect = humberto_image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    ball = humberto_rect
    player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 70, 10, 140)
    opponent = pygame.Rect(10, SCREEN_HEIGHT/2 - 70, 10, 140)

    bg_color = pygame.Color('grey12')
    light_grey = (200, 200, 200)

    ball_speed_x = 10 * random.choice((5, -5))
    ball_speed_y = 10 * random.choice((7, -7))
    player_speed = 0
    opponent_speed = 9

    # ===== Text Variable ===== #
    player_score = 0
    opponent_score = 0
    game_font = pygame.font.Font('assets/font/font.ttf', 32)

    # ========= Sounds ======== #
    pong_sound = pygame.mixer.Sound("assets/snd/pong.mp3")
    score_sound = pygame.mixer.Sound("assets/snd/score.mp3")

    # ===== Images ===== #
    GAMEBACKGROUND = pygame.image.load("assets/image/background.png").convert()

    # ===== Score Timer ===== #
    score_time = True

    while True:
        # ===== Handling Input ===== #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 6
                if event.key == pygame.K_UP:
                    player_speed -= 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 6
                if event.key == pygame.K_UP:
                    player_speed += 6
    
        # ===== Game Logic ===== #
        ball_animation()
        player_animation()
        opponent_ai()
        
        # ===== Visuals ===== #
        screen.fill(bg_color)
        SOLO_BACKGROUND = pygame.transform.scale(GAMEBACKGROUND, (1550, 810))
        screen.blit(SOLO_BACKGROUND, (0, 0))
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    
        if player_score == 3:
            WINNER()
        if opponent_score == 3:
            LOSE()
        if score_time:
            ball_restart()

        screen.blit(humberto_image, humberto_rect)
        
        player_text = game_font.render(f'{player_score}', False, light_grey)
        screen.blit(player_text, (850, 425))
    
        opponent_text = game_font.render(f'{opponent_score}', False, light_grey)
        screen.blit(opponent_text, (675, 425))
    
        
        # ===== Update The Window ===== #
        pygame.display.flip()
        clock.tick(60)
        

        


pygame.mixer.pre_init(44000,-16,2,512)
pygame.init()
SCREEN_WIDTH = 1550
SCREEN_HEIGHT = 810
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HUMBERPONG')


STARTBACKGROUND = pygame.image.load("assets/image/background.png").convert()
INSTRUCTIONBACKGROUND = pygame.image.load("assets/image/buttonsbackground.png").convert()
KEYS_ARROWS = pygame.image.load("assets/image/teclas_setas.png")
KEYS_WASD = pygame.image.load("assets/image/teclas_WASD.png")

menu_sound = pygame.mixer.Sound("assets/snd/menu.mp3")

def SOLO():
    while True:
        SOLO_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        SOLO_TEXT = get_font(20).render("Use as setinhas para movimentar seu jogador!", True, "White")
        SOLO_RECT = SOLO_TEXT.get_rect(center=(750, 100))
        SOLO_BACKGROUND = pygame.transform.scale(INSTRUCTIONBACKGROUND, (1550, 810))
        screen.blit(SOLO_BACKGROUND, (0, 0))
        screen.blit(SOLO_TEXT, SOLO_RECT)
        screen.blit(KEYS_ARROWS, (450, 150))
        
        SOLO_START = Button(image=None, pos=(1075, 700), 
                            text_input="START", font=get_font(75), base_color="White", hovering_color="Green")
        SOLO_BACK = Button(image=None, pos=(450, 700), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        SOLO_BACK.changeColor(SOLO_MOUSE_POS)
        SOLO_BACK.update(screen)
        SOLO_START.changeColor(SOLO_MOUSE_POS)
        SOLO_START.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SOLO_BACK.checkForInput(SOLO_MOUSE_POS):
                    main_menu()
                if SOLO_START.checkForInput(SOLO_MOUSE_POS):
                    pygame.mixer.Sound.stop(menu_sound)
                    sologame()
        pygame.display.update()
    
def PVP():
    while True:
        PVP_MOUSE_POS = pygame.mouse.get_pos()


        screen.fill("black")
        
        PVP_TEXT1 = get_font(20).render("Player 1 ", True, "White")
        PVP_TEXT2 = get_font(20).render("Player 2 ", True, "White")
        PVP_RECT1 = PVP_TEXT1.get_rect(center=(400, 130))
        PVP_RECT2 = PVP_TEXT1.get_rect(center=(1075, 130))
        PVP_BACKGROUND = pygame.transform.scale(INSTRUCTIONBACKGROUND, (1550, 810))
        screen.blit(PVP_BACKGROUND, (0, 0))
        screen.blit(PVP_TEXT1, PVP_RECT1)
        screen.blit(PVP_TEXT2, PVP_RECT2)
        screen.blit(KEYS_WASD, (120, 100))
        screen.blit(KEYS_ARROWS, (780, 150))


        PVP_START = Button(image=None, pos=(1075, 700), 
                            text_input="START", font=get_font(75), base_color="White", hovering_color="Green")
        PVP_BACK = Button(image=None, pos=(450, 700), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        PVP_BACK.changeColor(PVP_MOUSE_POS)
        PVP_BACK.update(screen)
        PVP_START.changeColor(PVP_MOUSE_POS)
        PVP_START.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PVP_BACK.checkForInput(PVP_MOUSE_POS):
                    main_menu()
                if PVP_START.checkForInput(PVP_MOUSE_POS):
                    pygame.mixer.Sound.stop(menu_sound)
                    pvpgame()

        pygame.display.update()

def main_menu():
    while True:
        
        pygame.mixer.Sound.play(menu_sound)
        
        BG = pygame.transform.scale(STARTBACKGROUND, (1550, 810))
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("HUMBERPONG", True, "Purple")
        MENU_RECT = MENU_TEXT.get_rect(center=(740, 150))

        SOLO_BUTTON = Button(image=pygame.image.load("assets/image/Play Rect.png"), pos=(740, 350), 
                            text_input="SOLO", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PVP_BUTTON = Button(image=pygame.image.load("assets/image/Options Rect.png"), pos=(740, 500), 
                            text_input="1V1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/image/Quit Rect.png"), pos=(740, 650), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [SOLO_BUTTON, PVP_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
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

   
