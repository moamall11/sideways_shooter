import pygame
import json

class ScoreBoard:
	"""the scoreboard of the game"""
	def __init__(self,game):
		"""initialize the attributes of the scoring system"""
		self.screen=game.screen
		self.settings=game.settings
		self.screen_rect=self.screen.get_rect()
		self.width,self.height=200,50
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.right=self.screen_rect.right
		self.rect.y=10
		self.font=pygame.font.SysFont(None,48)
		self.text_color=(50,50,50)
		self.high_score=self.get_saved_high_score()
		self.text_color2=(0,200,0)
		self.level=0
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.high_score_sound=True


	def prep_score(self):
		"""prepare the score"""
		score_str=str(self.settings.score)
		self.img=self.font.render(
			score_str,True,self.text_color,self.settings.bg_color)
		self.img_rect=self.img.get_rect()
		self.img_rect.center=self.rect.center


	def check_high_score(self):
		"""update the high score if there is a new high score"""
		if self.settings.score > self.high_score:
			self.high_score=self.settings.score
			self.prep_high_score()
			if self.high_score_sound:
				pygame.mixer.Sound("sounds/high_score.ogg").play()
				self.high_score_sound=False



	def prep_high_score(self):
		"""prepare the high score"""
		high_score_str=str(self.high_score)
		self.img2=self.font.render(
			high_score_str,True,self.text_color2,self.settings.bg_color)
		self.img2_rect=self.img2.get_rect()
		self.img2_rect.centerx=self.screen_rect.centerx
		self.img2_rect.y=10

	def get_saved_high_score(self):
		"""return the high score from the file if it exists"""
		try:
			with open("high_score.json") as file:
				saved_score=json.load(file)
		except FileNotFoundError:
			return 0
		else:
			return saved_score


	def prep_level(self):
		"""prep the image of the level"""
		settings=self.settings
		level_str=str(self.level)
		self.level_img=self.font.render(
			level_str,None,self.text_color,settings.bg_color)
		if self.level>=5:
			self.level_img=self.font.render(
				level_str,None,settings.bullet_color,settings.bg_color)
		self.level_rect=self.level_img.get_rect()
		self.level_rect.top+=50
		self.level_rect.right=self.rect.right

	def draw_score(self):
		"""draw the score to the screen"""
		self.screen.blit(self.img,self.img_rect)
		self.screen.blit(self.img2,self.img2_rect)
		self.screen.blit(self.level_img,self.level_rect)