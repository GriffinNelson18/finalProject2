import pygame
class Ship():

    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerxself.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        #Draw the ship at its current location (updates it)
        self.screen.blit(self.image, self.rect)