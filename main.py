'''
import pygame, sys
from pygame import *

pygame.init()

pygame.display.set_mode((500,500))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

            '''