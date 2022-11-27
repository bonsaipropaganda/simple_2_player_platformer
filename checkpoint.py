from settings import *
from tile import Tile

class CheckPoint(Tile):
	def __init__(self,pos,group,color):
		super().__init__(pos,group,color)
		self.image = pygame.image.load('checkpoint.png').convert_alpha()