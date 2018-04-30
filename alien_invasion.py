import sys
import pygame
from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
    #initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    #makes the ship v
    ship = Ship(screen)

    #CHANGE COLOR LATER V
    bg_color = (230, 230, 230)

    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()