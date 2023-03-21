import pygame
from pygame.locals import *
from sys import exit
from random import randint
from record import *


pygame.init()

music = pygame.mixer.music.load('bandidoazul.wav')
pygame.mixer.music.play(-1)
died_sound = pygame.mixer.Sound('cobalion.wav')
eat_sound = pygame.mixer.Sound('eat.wav')
first_goal = pygame.mixer.Sound('100points.wav')

width = 640
height = 480

x_snake = int(width / 2)
y_snake = int(height / 2)
x_apple = randint(40, 600)
y_apple = randint(50, 430)

velocity = 10
x_control = velocity
y_control = 0

died = False

points = 0
font = pygame.font.SysFont('arial', 20, True, True)
file = 'points.txt'


body_list = list()
initial_length = 5

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('SNAKE GAME')
clock = pygame.time.Clock()


def restart_game():
    global points, x_snake, y_snake, x_apple, y_apple, initial_length, head_list, body_list, died
    points = 0
    x_snake = int(width / 2)
    y_snake = int(height / 2)
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    initial_length = 5
    head_list = []
    body_list = []
    pygame.mixer.music.play()
    died = False


def increases(bs):
    for XeY in bs:
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


while True:
    clock.tick(30)
    screen.fill((92, 64, 90))
    msg = f'Points: {points}'
    formatted_text = font.render(msg, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == velocity:
                    pass
                else:
                    x_control = -velocity
                    y_control = 0
            if event.key == K_d:
                if x_control == -velocity:
                    pass
                else:
                    x_control = velocity
                    y_control = 0
            if event.key == K_s:
                if y_control == -velocity:
                    pass
                else:
                    x_control = 0
                    y_control = velocity
            if event.key == K_w:
                if y_control == velocity:
                    pass
                else:
                    x_control = 0
                    y_control = -velocity

    x_snake += x_control
    y_snake += y_control

    snake = pygame.draw.rect(screen, (0, 255, 0), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(screen, (255, 0, 0), (x_apple, y_apple, 20, 20))

    head_list = list()
    head_list.append(x_snake)
    head_list.append(y_snake)

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        points += 1
        initial_length += 1
        eat_sound.play()
        if points == 100:
            first_goal.play()

    body_list.append(head_list)

    if body_list.count(head_list) > 1:
        died_sound.play()
        font2 = pygame.font.SysFont('arial', 20, True, True)
        msg_final = 'Game Over! Press R to play again'
        formatted_text2 = font2.render(msg_final, True, (255, 255, 255))
        rect_txt = formatted_text2.get_rect()
        record(file, points)


        died = True
        while died:
            pygame.mixer.music.stop()
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()
            rect_txt.center = (width // 2, height // 2)
            screen.blit(formatted_text2, rect_txt)
            screen.blit(formatted_text, (250, 260))
            pygame.display.update()

    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake > height:
        y_snake = 0
    if y_snake < 0:
        y_snake = height

    increases(body_list)

    if len(body_list) > initial_length:
        del body_list[0]

    screen.blit(formatted_text, (470, 15))
    pygame.display.update()
