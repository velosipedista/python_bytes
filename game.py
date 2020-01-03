import os, sys
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((468, 60))
pygame.display.set_caption('Snake byte')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Press space to start game", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)
    
screen.blit(background, (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
while 1:
    clock.tick(60)
