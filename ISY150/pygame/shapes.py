import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()
    # surface, color, Rect, width
    pygame.draw.rect(screen, (140, 240, 130), Rect((100, 100), (130, 170)))
    screen.unlock()

    pygame.display.update()