import pygame, sys, random
from soloend import WINNER
from soloend import LOSE

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
    ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 - 15, 30, 30)
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
            WINNER()
        if score_time:
            ball_restart()
    
        player_text = game_font.render(f'{player_score}', False, light_grey)
        screen.blit(player_text, (850, 425))
    
        opponent_text = game_font.render(f'{opponent_score}', False, light_grey)
        screen.blit(opponent_text, (675, 425))
    
        
        # ===== Update The Window ===== #
        pygame.display.flip()
        clock.tick(60)
        