import pygame
import pygame.font
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
        pygame.init()

        self.loaded = False
        self.WIDTH = TILESIZE * 10
        self.HEIGHT = TILESIZE * 15
        self.FONT = pygame.font.Font("freesansbold.ttf", 32)
        self.TILESIZE = TILESIZE
        
        # COLORS
        self.TRANSPARENT = (0,0,0,0)
        self.WHITE = (255,255,255,255)
        self.OFF_WHITE = (255,255,255,100)
        self.GREY = (51,51,51,255)
        self.RED = (255,0,0,255)

        # GAME COLORS
        self.BG_COLOR = self.GREY
        self.BORDER_COLOR = self.OFF_WHITE
        self.BUTTON_COLOR = self.RED
        self.BUTTON_TEXT_COLOR = self.WHITE

        # DICE
        self.DICESURFACE = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        self.DICESURFACE.fill(self.BG_COLOR)
        self.DICE_ROLL_GIFS = {}
        self.DICE_NUM = randint(1,6)
        self.DICE_anim_framecount = 0

        # BUTTON
        self.BUTTONSURFACE = pygame.Surface((4*TILESIZE, 1*TILESIZE), pygame.SRCALPHA)
        self.BUTTONSURFACE.fill(self.BUTTON_COLOR)
        text = self.FONT.render("ROLL!", True, self.BUTTON_TEXT_COLOR, self.BUTTON_COLOR)
        rect = text.get_rect()
        rect.center = self.BUTTONSURFACE.get_rect().center
        self.BUTTONSURFACE.blit(text, rect)
        self.BUTTONRECT = pygame.Rect(3*self.TILESIZE, 12 * self.TILESIZE,4*self.TILESIZE, 1*self.TILESIZE)
        self.BUTTON_clickable = True

        # ANIMATION
        self.BORDER_ANIMATION_SURFACE = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        self.animation_angle = 0
        self.delta_angle = 30
    
    def loadGIFS(self):
        for i in range(1,7):
            self.DICE_ROLL_GIFS[i] = loadGIF(f"assets\{i}.gif")
        self.loaded = True
    
    def buttonListener(self, pos):
        if self.BUTTONRECT.collidepoint(pos[0] - self.TILESIZE * 15, pos[1]) :
            if self.BUTTON_clickable:
                self.DICE_NUM = randint(1,6)
                self.DICE_anim_framecount = 0
                self.BUTTON_clickable = False


    def update(self):
        pass
        
        # uncomment to turn on border
        # self.Border_animation()
        # self.DICESURFACE.blit(self.BORDER_ANIMATION_SURFACE,( 0, 0, self.WIDTH, self.HEIGHT))
    
    def draw(self):
        self.DICESURFACE.fill(self.BG_COLOR)
        self.DICESURFACE.blit(self.BUTTONSURFACE, self.BUTTONRECT)
        self.roll_dice()

    def roll_dice(self):
        gifFrameList = self.DICE_ROLL_GIFS[self.DICE_NUM]
        rect = (0,0,gifFrameList[self.DICE_anim_framecount].get_width(), gifFrameList[self.DICE_anim_framecount].get_height())
        self.DICESURFACE.blit(gifFrameList[self.DICE_anim_framecount], rect)
        # currentFrame = (currentFrame + 1) % len(gifFrameList)
        self.DICE_anim_framecount = (self.DICE_anim_framecount + (1 if self.DICE_anim_framecount != (len(gifFrameList)-1) else 0 ))#+ 1) % len(gifFrameList)
        if self.DICE_anim_framecount == (len(gifFrameList)-1):
            self.BUTTON_clickable = True

    def Border_animation(self):
        self.BORDER_ANIMATION_SURFACE.fill(self.TRANSPARENT)
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (0,0),(0,self.HEIGHT))
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (self.WIDTH,0),(self.WIDTH,self.HEIGHT))
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (0,0),(self.WIDTH,0))
        pygame.draw.aaline(self.BORDER_ANIMATION_SURFACE, self.BORDER_COLOR, (0,self.HEIGHT),(self.WIDTH,self.HEIGHT))
        self.animation_angle += 0.1
