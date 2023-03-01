import pygame
import sys

TILESIZE = 60
SIZE = WIDTH,HEIGHT = (25 * TILESIZE, 15 * TILESIZE)
SCREEN = pygame.display.set_mode(SIZE, pygame.SRCALPHA)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    SCREEN.fill((0,0,0,0))

    pygame.display.flip()
