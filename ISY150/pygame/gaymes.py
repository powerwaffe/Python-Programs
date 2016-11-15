import pygame, sys
from pygame.locals import *

bif = "C:\\Users\\Sean\\Pictures\\images\\black.jpg"
mif = "C:\\Users\\Sean\\Pictures\\images\\bluedot.png"

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)
background = pygame.image.load(bif).convert()
mouse_c = pygame.image.load(mif).convert_alpha()

x, y = 0, 0
moveX, moveY = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveX = -1
            elif event.key == K_RIGHT:
                moveX = +1
            elif event.key == K_UP:
                moveY = -1
            elif event.key == K_DOWN:
                moveY = +1
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveX = 0
            elif event.key == K_RIGHT:
                moveX = 0
            elif event.key == K_UP:
                moveY = 0
            elif event.key == K_DOWN:
                moveY = 0

    x += moveX
    y += moveY

    screen.blit(background, (0, 0))
    screen.blit(mouse_c, (x, y))

    pygame.display.update()
