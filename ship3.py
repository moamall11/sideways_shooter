import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""manage the ship's assets and behavior"""
	def __init__(self,game):
		"""initialize the attributes of the ship"""
		super().__init__()
		self.settings=game.settings
		#the screen properties
		self.screen=game.screen
		self.screen_rect=game.screen.get_rect()
		#the ship properties
		self.image=pygame.image.load("images/ship.bmp")
		self.rect=self.image.get_rect()
		#set it's starting position
		self.rect.midleft=self.screen_rect.midleft
		#decimal value of the rect of the ship
		self.y=float(self.rect.y)
		#moving flags
		self.moving_up=False
		self.moving_down=False

	def update(self):
		"""update the position of the ship"""
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed3
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed3
		self.rect.y = self.y

	def blitme(self):
		"""put the image on the screen in it's current position"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""put the ship in the center of the bottom of the screen"""
		self.rect.midleft = self.screen_rect.midleft
		self.y=float(self.rect.y)

