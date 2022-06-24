import pygame as pg
from pygame.sprite import Sprite

class Explosion(Sprite):
	"""manage the explosion of the aliens"""
	def __init__(self,game):
		"""initialize the attributes of the explosion"""
		super().__init__()
		self.settings=game.settings
		self.screen=game.screen

		self.image=pg.image.load("images/explosion.bmp")
		self.rect=self.image.get_rect()
