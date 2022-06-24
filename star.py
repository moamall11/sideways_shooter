import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""manage the object star"""
	def __init__(self,game):
		"""initialize the attributes of the star"""
		super().__init__()
		self.settings=game.settings
		self.screen=game.screen
		#set the image and the rect.
		self.image=pygame.image.load('star.bmp')
		self.rect=self.image.get_rect()
		#set the initial position.
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		#store the decimal value of the horizontal rect.
		self.x=float(self.rect.x)