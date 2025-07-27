import pygame
from pygame.locals import *
pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

#colors:
bg = (50, 25, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

#variables
margin = 50
white = (255, 255, 255)
cpu_score = 0
player_score = 0


def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (SCREEN_WIDTH, margin))


run = True
while run:
 
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
