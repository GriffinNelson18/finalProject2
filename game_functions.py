import sys
import pygame

def check_events(ship):
	#Keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				if ship.rect.centerx < 1150:
				# Move the ship to the right.
					ship.rect.centerx += 50
			if event.key == pygame.K_LEFT:
				if ship.rect.centerx > 50:
				# Move the ship to the right.
					ship.rect.centerx -= 50

def update_screen(ai_settings, screen, ship):
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# Make the most recently drawn screen visible.
	pygame.display.flip()
