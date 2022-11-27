import pygame
import sys
from level import Level
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level()

# main game
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('white')
	level.run()

	clock.tick(60)
	pygame.display.update()