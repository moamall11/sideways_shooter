import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """represent the alien"""
    def __init__(self,game):
        """initialize the attributes of the alien"""
        super().__init__()
        self.settings=game.settings
        self.screen=game.screen
        #add image and set the rect.
        self.image=pygame.image.load("images/image.bmp")
        self.rect=self.image.get_rect()
        #set the initial position.
        self.rect.x=self.settings.screen_width - self.rect.width
        self.rect.y=self.rect.height


    def check_edges(self):
        """return True when the alien reaches either edge of the screen"""
        if (self.rect.bottom >= self.screen.get_rect().bottom 
            or self.rect.top <= 0):
            return True
