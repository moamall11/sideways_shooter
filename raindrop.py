import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
	"""the object"""
	def __init__(self,game):
		"""initialize the attributes of the object"""
		super().__init__()
		self.settings=game.settings
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()
		#the image and rect of the object.
		self.image=pygame.image.load('drop.bmp')
		self.rect=self.image.get_rect()
		#the position.
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		#store the decimal value of the rect of the object.
		self.y=float(self.rect.y)


	def update(self):
		"""update the position of the drop"""
		self.y += self.settings.drop_speed
		self.rect.y = self.y


	def check_edge(self):
		"""return True if the drop has reached the bottom of the screen"""
		if self.rect.top >= self.screen_rect.bottom:
			return True
		else:
			return False