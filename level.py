from settings import *
from player import Player
from player2 import Player2
from tile import Tile
from checkpoint import CheckPoint

class Level:
	def __init__(self):
		# groups
		self.collision_sprites = pygame.sprite.Group()
		self.visible_sprites = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		self.check_points = pygame.sprite.Group()

		# basic setup
		self.screen = pygame.display.get_surface()
		self.create_map()

		

	def create_map(self):
		for col_number,col in enumerate(LEVEL_MAP):
			for row_number,row in enumerate(col):
				y = col_number * TILE_SIZE
				x = row_number * TILE_SIZE

				if row == 'C':
					CheckPoint((x,y),[self.check_points],'green')
				if row == 'P':
					self.player = Player((x,y),[self.visible_sprites],self.collision_sprites,self.enemy_sprites,self.check_points)
				if row == '2':
					self.player2 = Player2((x,y),[self.visible_sprites],self.collision_sprites,self.enemy_sprites,self.check_points)
				if row == 'X':
					Tile((x,y),[self.visible_sprites,self.collision_sprites],'grey')
				if row == 'G':
					Tile((x,y),[self.visible_sprites,self.collision_sprites],'yellow')
				if row == 'E':
					Tile((x,y),[self.visible_sprites,self.enemy_sprites],'red')


	def run(self):
		self.check_points.draw(self.screen)
		self.visible_sprites.draw(self.screen)
		self.visible_sprites.update()