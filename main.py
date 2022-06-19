#!/usr/bin/env python3
import pygame


WIDTH, HEIGHT = 800,500
PLAYER_WIDTH,PLAYER_LENGTH = 5,40

BLACK = 0,0,0
WHITE = 255,255,255

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("PONG")

FPS = 60

NET = []
NET_LENGTH = 12
NET_GAP = 8
i = 0
while i <= HEIGHT:
    NET.append(i)
    NET.append(i + NET_LENGTH)
    i += NET_GAP + NET_LENGTH



def draw_window(player1,player2):
    WIN.fill(BLACK)

    pygame.draw.rect(WIN,WHITE,player1)
    pygame.draw.rect(WIN,WHITE,player2)
    i = 0
    while i < len(NET):
        pygame.draw.line(WIN,WHITE,(WIDTH/2,NET[i]),(WIDTH/2, NET[i+1]))
        i += 2

    pygame.display.update()



def main():
    clock = pygame.time.Clock()

    player1 = pygame.Rect(40,HEIGHT / 2 - PLAYER_LENGTH / 2, PLAYER_WIDTH, PLAYER_LENGTH)
    player2 = pygame.Rect(WIDTH - 40 - PLAYER_WIDTH, HEIGHT / 2 - PLAYER_LENGTH / 2, PLAYER_WIDTH, PLAYER_LENGTH)
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window(player1,player2,net)




if __name__ == "__main__":
    main()

