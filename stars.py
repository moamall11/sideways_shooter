import pygame
import sys
from star_settings import Settings 
from star import Star
from random import randint

class Stars:
    """the game"""
    def __init__(self):
        """initialize the game's attributes"""
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.stars=pygame.sprite.Group()
        pygame.display.set_caption("Stars")
        self.star_numbers=randint(-10,10)
        self.star_rows=randint(-6,6)
        self._create_stars()


    def run_game(self):
        """the main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self._update_screen()


    def _create_stars(self):
        """add a star to the group of stars"""
        star=Star(self)
        #set the width and height of each star.
        star_width,star_height=star.rect.size
        ran=randint(1,2)
        #find the available space to decide how many stars should we make.
        available_space_x=self.settings.screen_width - (star_width)
        available_space_y=self.settings.screen_height - (2*star_height)
        star_numbers=available_space_x // (ran * star_width) - self.star_numbers
        star_rows=available_space_y // (ran * star_height) - self.star_rows

        for row_number in range(star_rows):
            for star_number in range(star_numbers):
                self._create_star(star_number,row_number)

    
    def _create_star(self,star_number,row_number):
        """make a new star instance and add it to the group"""
        star=Star(self)
        star_width,star_height=star.rect.size
        ran=randint(1,5)
        star.x=star_width + ran * star_width * star_number 
        star.rect.x=star.x
        star.rect.y=star_height + ran * star_height * row_number
        self.stars.add(star)


    def _update_screen(self):
        """update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__=='__main__':
    game=Stars()
    game.run_game()




