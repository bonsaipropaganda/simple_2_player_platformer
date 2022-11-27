from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups,color):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft = pos)