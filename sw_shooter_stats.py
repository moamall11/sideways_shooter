class Stats:
	"""represent the game statistics"""
	def __init__(self,game):
		"""initialize the statistics of the game"""
		self.settings=game.settings
		self.reset_stats()
		#set the initial state of the game.
		self.game_active=False


	def reset_stats(self):
		"""initialize the statistics that change during the game"""
		self.ships_left=self.settings.ship_limit