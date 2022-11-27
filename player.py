from settings import *
# from platform import Platform

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,collision_sprites,enemy_sprites,checkpoints):
		super().__init__(groups)
		# basic player attrs
		self.pos = pos
		self.start_pos = pygame.math.Vector2(143,520)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image.fill('black')
		self.rect = self.image.get_rect(topleft = pos)

		# movement
		self.speed = 5
		self.direction = pygame.math.Vector2()

		# jumping and negative jumping
		self.gravity = .6
		self.jump_speed = -11
		self.is_on_floor = False

		# collisions
		self.collision_sprites = collision_sprites
		self.enemy_sprites = enemy_sprites

		# checkpoints
		self.checkpoints = checkpoints


	# movement
	def get_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else: self.direction.x = 0

		if keys[pygame.K_UP]:
		 	self.jump()

	def move(self):
		self.get_input()
		self.rect.x += self.speed * self.direction.x

	def jump(self):
		if self.is_on_floor == True:
			self.direction.y = self.jump_speed
			self.is_on_floor = False


	# collisions
	def collisions_horizontal(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):

					# horizontal collisions
					if self.direction.x > 0:
						self.rect.right = sprite.rect.left
					elif self.direction.x < 0:
						self.rect.left = sprite.rect.right

	def collisions_vertical(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
					if self.direction.y > 0:
						self.direction.y = 0
						self.rect.bottom = sprite.rect.top
						self.is_on_floor = True
						
					if self.direction.y < 0:
						self.direction.y = 0
						self.rect.top = sprite.rect.bottom


	def lava_collisions(self):
		for sprite in self.enemy_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				self.rect.center = self.start_pos

	def checkpoint(self):
		for sprite in self.checkpoints.sprites():
			if sprite.rect.colliderect(self.rect):
				self.start_pos = sprite.rect.topleft


	# making the player fall and sometimes not fall
	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def update(self):
		# player movement and collisions and physics
		self.move()
		self.collisions_horizontal()
		self.apply_gravity()
		self.collisions_vertical()
		self.lava_collisions()
		self.checkpoint()