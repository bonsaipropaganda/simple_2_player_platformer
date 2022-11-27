from player import Player
from settings import *

class Player2(Player):
	def __init__(self,pos,groups,collision_sprites,enemy_sprites,checkpoints):
		super().__init__(pos,groups,collision_sprites,enemy_sprites,checkpoints)

		self.image.fill('blue')

	def get_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_a]:
			self.direction.x = -1
		else: self.direction.x = 0

		if keys[pygame.K_w]:
		 	self.jump()