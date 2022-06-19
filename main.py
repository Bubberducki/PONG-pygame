#!/usr/bin/env python3
import pygame
import random
import math

pygame.font.init()
pygame.mixer.init()

PIXEL_FONT = pygame.font.Font("Assets/Pixeled.ttf",50)

HIT_SOUND = pygame.mixer.Sound("Assets/hit_sound.wav")
HIT_SOUND_2 = pygame.mixer.Sound("Assets/hit_sound_2.wav")
SCORE_SOUND = pygame.mixer.Sound("Assets/score_sound.mp3")
WIN_SOUND = pygame.mixer.Sound("Assets/win_sound.wav")



WIDTH, HEIGHT = 800,500
PLAYER_WIDTH,PLAYER_LENGTH = 5,50
BALL_DIA = 10

BLACK = 0,0,0
WHITE = 255,255,255

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("PONG")


FPS = 60
PLAYER_VEL = 10

P1_SCORE = pygame.USEREVENT + 1
P2_SCORE = pygame.USEREVENT + 2






NET = []
NET_LENGTH = 12
NET_GAP = 8
i = 0
while i <= HEIGHT:
    NET.append(i)
    NET.append(i + NET_LENGTH)
    i += NET_GAP + NET_LENGTH



def draw_window(player1,player2,ball,score_p1,score_p2):
    WIN.fill(BLACK)

    score_p1_text = PIXEL_FONT.render(str(score_p1),1,WHITE)
    score_p2_text = PIXEL_FONT.render(str(score_p2),1,WHITE)



    pygame.draw.rect(WIN,WHITE,player1)
    pygame.draw.rect(WIN,WHITE,player2)
    pygame.draw.ellipse(WIN,WHITE,ball)
    WIN.blit(score_p1_text,(WIDTH/3 - score_p1_text.get_width(), 10))
    WIN.blit(score_p2_text,(WIDTH/3 * 2 + 7, 10))

    i = 0
    while i < len(NET):
        pygame.draw.line(WIN,WHITE,(WIDTH/2-1,NET[i]),(WIDTH/2-1, NET[i+1]))
        i += 2

    pygame.display.update()



def control_player1(keys_pressed,player1):
    if keys_pressed[pygame.K_s] and player1.y + PLAYER_LENGTH < HEIGHT:
        player1.y += PLAYER_VEL#DOWN

    if keys_pressed[pygame.K_w] and player1.y > 0:
        player1.y -= PLAYER_VEL#UP


def control_player2(keys_pressed,player2):
    if keys_pressed[pygame.K_DOWN] and player2.y + PLAYER_LENGTH < HEIGHT:
        player2.y += PLAYER_VEL#DOWN

    if keys_pressed[pygame.K_UP] and player2.y > 0:
        player2.y -= PLAYER_VEL#UP



def ball_move(ball,BALL_SPEED_X,BALL_SPEED_Y):

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y


def reset(ball,player1,player2):
    player1.x, player1.y = 40,HEIGHT / 2 - PLAYER_LENGTH / 2
    player2.x, player2.y = WIDTH - 40 - PLAYER_WIDTH, HEIGHT / 2 - PLAYER_LENGTH / 2
    ball.x,ball.y = WIDTH / 2 - BALL_DIA / 2, HEIGHT / 2 - BALL_DIA / 2 + random.randint(-200,200)
    HIT_SOUND_2.play()

def draw_win_text(win_text):
    draw_text = PIXEL_FONT.render(win_text,1,WHITE)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height() /2))
    pygame.display.update()
    pygame.time.delay(5000)

def random_speed():
    speed_list = [-5,-4,-3,3,4,5]
    direction = [-1,1]

    BALL_SPEED_X = random.choice(speed_list)
    BALL_SPEED_Y = int(math.sqrt(49 - BALL_SPEED_X**2)) * random.choice(direction)

    return BALL_SPEED_X,BALL_SPEED_Y


    



def main():
    clock = pygame.time.Clock()

    player1 = pygame.Rect(40,HEIGHT / 2 - PLAYER_LENGTH / 2, PLAYER_WIDTH, PLAYER_LENGTH)
    player2 = pygame.Rect(WIDTH - 40 - PLAYER_WIDTH, HEIGHT / 2 - PLAYER_LENGTH / 2, PLAYER_WIDTH, PLAYER_LENGTH)
    score_p1 = 0
    score_p2 = 0

    ball = pygame.Rect(WIDTH / 2 - BALL_DIA / 2, HEIGHT / 2 - BALL_DIA / 2, BALL_DIA, BALL_DIA)

    BALL_SPEED_X,BALL_SPEED_Y = random_speed()

    run = True
    HIT_SOUND_2.play()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        if ball.y <= 0 or ball.y + BALL_DIA >= HEIGHT:
            BALL_SPEED_Y *= -1
            HIT_SOUND_2.play()
        if player1.colliderect(ball) or player2.colliderect(ball):
            BALL_SPEED_X *= -1
            HIT_SOUND.play()




        if ball.x >= WIDTH:
            score_p1 += 1
            SCORE_SOUND.play()
            pygame.time.delay(2000)
            BALL_SPEED_X,BALL_SPEED_Y = random_speed()
            reset(ball,player1,player2)
        if ball.x <= -BALL_DIA:
            score_p2 += 1
            SCORE_SOUND.play()
            pygame.time.delay(2000)
            BALL_SPEED_X,BALL_SPEED_Y = random_speed()
            reset(ball,player1,player2)

        win_text = ""
        if score_p1 >= 10:
            win_text = "P1 WINS !"
        if score_p2 >= 10:
            win_text = "P2 WINS !"

        if win_text != "":
            WIN_SOUND.play()
            draw_win_text(win_text)
            break







        ball_move(ball,BALL_SPEED_X,BALL_SPEED_Y)
        keys_pressed = pygame.key.get_pressed()
        control_player1(keys_pressed,player1)
        control_player2(keys_pressed,player2)
        draw_window(player1,player2,ball,score_p1,score_p2)

    main()




if __name__ == "__main__":
    main()

