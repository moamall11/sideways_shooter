import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""manage the bullet's assets and behavior"""
	def __init__(self,game):
		"""initialize the attributes of the bullet"""
		super().__init__()
		self.settings=game.settings
		self.screen=game.screen
		#create the rect at (0,0).
		self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
		#set the initial position
		self.rect.midright=game.ship.rect.midright
		#make a decimal value.
		self.x=float(self.rect.x)
		self.color=self.settings.bullet_color


	def update(self):
		"""update the position of the bullet"""
		self.x += self.settings.bullet_speed2

		self.rect.x = self.x

	def draw_bullet(self):
		"""draw the bullet to the screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)