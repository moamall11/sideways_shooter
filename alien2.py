import pygame
from random import randint
from pygame.sprite import Sprite
class Alien(Sprite):
    """represent the alien"""
    def __init__(self,game):
        """initialize the attributes of the alien"""
        super().__init__()
        self.settings=game.settings
        self.screen=game.screen
        #add image and set the rect.
        self.image=pygame.image.load("images/alien.bmp")
        self.rect=self.image.get_rect()
        #set the initial position.
        self.rect.x=self.settings.screen_width - self.rect.width
        self.max_y=self.settings.screen_height - self.rect.height
        self.rect.top=randint(0,self.max_y)
        self.x=float(self.rect.x)


    def update(self):
        """update the position"""
        self.x -= self.settings.aliens_speed3
        self.rect.x = self.x