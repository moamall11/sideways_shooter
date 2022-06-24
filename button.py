import pygame.font
import pygame

class Button:
	"""button"""
	def __init__(self,game,msg):
		"""initialize the button attributes"""
		self.screen=game.screen
		self.settings=game.settings
		self.screen_rect=self.screen.get_rect()
		#button properties.
		self.button_color=(0,255,0)
		self.text_color=(255,255,255)
		self.width,self.height=200,50
		self.font=pygame.font.SysFont(None,48)
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		self.prep_msg(msg)


	def prep_msg(self,msg):
		"""convert msg into an image"""
		self.img=self.font.render(msg,True,self.text_color,self.button_color)
		self.img_rect=self.img.get_rect()
		self.img_rect.center=self.rect.center

	def draw_button(self):
		"""draw the button and the msg to the screen"""
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.img,self.img_rect)
