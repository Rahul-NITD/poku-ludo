import pygame
from PIL import Image, ImageSequence
from random import randint

def pilImageToSurface(pilImage):
    mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
    return pygame.image.fromstring(data, size, mode).convert_alpha()

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    if pilImage.format == 'GIF' and pilImage.is_animated:
        for frame in ImageSequence.Iterator(pilImage):
            pygameImage = pilImageToSurface(frame.convert('RGBA'))
            frames.append(pygameImage)
    else:
        frames.append(pilImageToSurface(pilImage))
    return frames

class Dice():
    def __init__(self, TILESIZE) -> None:
        self.loaded = False
        self.WIDTH = TILESIZE * 10
        self.HEIGHT = TILESIZE * 15
        
        # COLORS
        self.TRANSPARENT = (0,0,0,0)
        self.WHITE = (255,255,255,255)
        self.OFF_WHITE = (255,255,255,100)
        self.GREY = (51,51,51,255)

        # GAME COLORS
        self.BG_COLOR = self.GREY
        self.BORDER_COLOR = self.OFF_WHITE

        # DICE
        self.DICESURFACE = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        self.DICESURFACE.fill(self.BG_COLOR)
        self.DICE_ROLL_GIFS = {}
        self.DICE_NUM = 1
        self.DICE_anim_framecount = 0

        # ANIMATION
        self.BORDER_ANIMATION_SURFACE = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        self.animation_angle = 0
        self.delta_angle = 30
    
    def loadGIFS(self):
        for i in range(1,7):
            self.DICE_ROLL_GIFS[i] = loadGIF(f"assets\{i}.gif")
        self.loaded = True

    def update(self):
        self.DICESURFACE.fill(self.BG_COLOR)
        self.roll_dice()
        # uncomment to turn on border
        # self.Border_animation()
        # self.DICESURFACE.blit(self.BORDER_ANIMATION_SURFACE,( 0, 0, self.WIDTH, self.HEIGHT))
    
    def roll_dice(self):
        gifFrameList = self.DICE_ROLL_GIFS[self.DICE_NUM]
        rect = (0,0,gifFrameList[self.DICE_anim_framecount].get_width(), gifFrameList[self.DICE_anim_framecount].get_height())
        self.DICESURFACE.blit(gifFrameList[self.DICE_anim_framecount], rect)
        # currentFrame = (currentFrame + 1) % len(gifFrameList)
        self.DICE_anim_framecount = (self.DICE_anim_framecount + (1 if self.DICE_anim_framecount != (len(gifFrameList)-1) else 0 ))#+ 1) % len(gifFrameList)

    def Border_animation(self):
        self.BORDER_ANIMATION_SURFACE.fill(self.TRANSPARENT)
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (0,0),(0,self.HEIGHT))
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (self.WIDTH,0),(self.WIDTH,self.HEIGHT))
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (0,0),(self.WIDTH,0))
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (0,self.HEIGHT),(self.WIDTH,self.HEIGHT))
        self.animation_angle += 0.1
