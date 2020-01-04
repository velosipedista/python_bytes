import os, sys
import pygame
from pygame.locals import *
class game:
    def __init__(self):
        pygame.init()
        
    def setViewPort(self, h, w):
        self.screen = pygame.display.set_mode((h, w))
        pygame.display.set_caption('Snake byte')
        pygame.mouse.set_visible(0)
        
    def setDefaultBG(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Press space to start game", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width()/2)
            background.blit(text, textpos)
        self.screen.blit(background, (0, 0))
        pygame.display.flip()
        
# snake = Game();
# snake.setViewPort(640,80);
# snake.setDefaultBG();
# clock = pygame.time.Clock()
# while 1:
#     clock.tick(60)
