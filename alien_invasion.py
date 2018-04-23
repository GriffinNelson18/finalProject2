import sys
import pygame
from ship import Ship
from settings import Settings

def run_game():
    #initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    #makes the ship v
    ship = Ship(screen)

    #CHANGE COLOR LATER V
    bg_color = (230, 230, 230)

    while True:
        #Keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        
        ship.blitme()

        pygame.display.flip()

run_game()