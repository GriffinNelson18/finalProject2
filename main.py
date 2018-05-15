#CUBEFIELD
#Full credit to 'Kids Can Code' for the game template and keystate function tutorials
import pygame
import random

#Wider to fit background
WIDTH = 960
HEIGHT = 600
FPS = 60
PROGRESS = 1
DIFFICULTY = 1

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# function that draws text on a screen using pygame elements
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# create new mob
def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteor Dodge")
clock = pygame.time.Clock()

class Glider(pygame.sprite.Sprite):
    #SPRITE PREREQUISITES
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        #mandatory piece number 2
        self.rect = self.image.get_rect()
        #puts ship in the center
        self.rect.centerx = WIDTH / 2
        #10 pixels up from the bottom
        self.rect.bottom = HEIGHT - 10
        #speed of the glider
        self.speedx = 0

    def update(self):
        self.speedx = 0
        #every key on the keyboard that is down in this instant
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.rect.x != 0:
            self.speedx = -10
        if keystate[pygame.K_RIGHT] and self.rect.x != WIDTH - self.rect.width:
            self.speedx = 10
        #controls how fast it updates
        self.rect.x += self.speedx

#variable to allow color change
mobColor = RED

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(mobColor)
        #get position
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        self.rect.y += 10 + DIFFICULTY

    # def colorchange(self):
    #     for n in mobColor:
    #         n += 1
        


#Create sprite group for all sprites
all_sprites = pygame.sprite.Group()
#Create mobs sprite group
mobs = pygame.sprite.Group()
player = Glider()
#adds our glider to the sprites file above
all_sprites.add(player)

newmob()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    #Add points
    PROGRESS += 1
    # Update
    all_sprites.update()

    if PROGRESS % 10 == 0:
        newmob()

    if PROGRESS % 100 == 0:
        DIFFICULTY += 1
        '''If you do not want to play with increasing difficulty, simply comment out the line
        above and uncomment the line below.'''
        #DIFFICULTY = 1

    

    #End game upon collision
    hits = pygame.sprite.spritecollide(player, mobs, True)
    for hit in hits:
        running = False

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, str(PROGRESS), 34, WIDTH/2, 10)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
