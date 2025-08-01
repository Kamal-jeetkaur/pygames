import pygame
from pygame.locals import *
pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
FPS = pygame.time.Clock()
fps = 60

#colors:
bg = (50, 25, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

#fonts
font = pygame.font.SysFont('Asap', 30)

#variables
margin = 50
white = (255, 255, 255)
cpu_score = 0
player_score = 0


def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (SCREEN_WIDTH, margin))

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 20, 100)
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)
        elif key[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, self.speed)

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

class BALL():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ball_radius = 8
        self.rect = Rect(self.x, self.y, self.ball_radius *2, self.ball_radius*2)
        self.speed_x = -5
        self.speed_y = 5

    def move(self):
        #update ball position
        self.rect.x += self.rect.x
        self.rect.y += self.rect.y


    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius) 

#paddles    
player_paddle = Paddle(SCREEN_WIDTH - 40, SCREEN_HEIGHT//2)
cpu_paddle = Paddle(20, SCREEN_HEIGHT//2)

#pong ball
pong_ball = BALL(SCREEN_WIDTH - 60, SCREEN_HEIGHT//2 + 50)


run = True
while run:
 
    FPS.tick(fps)
 
    draw_board()
    draw_text('CPU: '+str(cpu_score), font, white, 20, 15)
    draw_text('P1: '+str(player_score), font, white, SCREEN_WIDTH - 100 , 15)


    player_paddle.draw()
    cpu_paddle.draw()

    #draw ball
    pong_ball.draw()

    #move paddle
    player_paddle.move()

    #move ball
    pong_ball.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
