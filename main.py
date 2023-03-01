import pygame
import sys
from Dice import Dice

TILESIZE = 50
FPS = 60
SIZE = WIDTH,HEIGHT = (25 * TILESIZE, 15 * TILESIZE)
SCREEN = pygame.display.set_mode(SIZE, pygame.SRCALPHA)
CLOCK = pygame.time.Clock()

dice = Dice(TILESIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    SCREEN.fill((0,0,0,0))
    SCREEN.blit(dice.DICESURFACE, (15*TILESIZE, 0, dice.WIDTH, dice.HEIGHT))

    pygame.display.flip()
    CLOCK.tick(FPS)
