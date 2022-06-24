import pygame
import sys
from raindrop_settings import Settings
from raindrop import Raindrop

class Raindrops:
	"""the game"""
	def __init__(self):
		"""initialize the attributes of the game"""
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Raindrops")
		self.drops=pygame.sprite.Group()
		self._create_drops()



	def run_game(self):
		"""the main loop"""
		while True:
			self._check_events()
			self.drops.update()
			self._check_drops()
			self._update_screen()

	def _check_events(self):
		"""check and respond to events"""
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()

	def _create_drops(self):
		"""create a group of drops"""
		drop=Raindrop(self)
		drop_width,drop_height=drop.rect.size
		available_space_x=self.settings.screen_width - (2 * drop_width)
		self.number_drops_x=available_space_x // (2 * drop_width)
		number_rows=self.settings.screen_height // (2 * drop_height)
		for number_row in range(number_rows):
			for drop_number in range(self.number_drops_x):
				self._create_drop(number_row,drop_number)

	def _create_drop(self,number_row,drop_number):
		"""make a new drop and add it to the group"""
		drop=Raindrop(self)
		drop_width,drop_height=drop.rect.size
		drop.rect.x = drop_width + 2 * drop_width * drop_number
		drop.y=drop_height + 2 * drop_height * number_row
		drop.rect.y=drop.y
		self.drops.add(drop)


	def _check_drops(self):
		"""create a new group of drops 
		when the previous group disappeares from the screen"""
		make_drops=False
		for drop in self.drops.sprites():
			if drop.check_edge():
				self.drops.remove(drop)
				make_drops=True
		if make_drops:
			for drop_number in range(self.number_drops_x):
				self._create_drop(0,drop_number)



	def _update_screen(self):
		"""update the screen"""
		self.screen.fill(self.settings.bg_color)
		self.drops.draw(self.screen)
		pygame.display.flip()

if __name__=='__main__':
	game=Raindrops()
	game.run_game()