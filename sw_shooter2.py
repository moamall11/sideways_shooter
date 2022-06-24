import pygame as pg
from random import randint
import sys
from time import sleep
import json

from shooter_settings import Settings
from ship2  import Ship
from bullet2 import Bullet
from alien import Alien
from sw_shooter_stats import Stats
from button import Button 
from score_board2 import ScoreBoard as SB

class Shooter():
    """the game"""
    def __init__(self):
        pg.init()
        self.settings=Settings()
        self.screen=pg.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.ship=Ship(self)
        self.bullets=pg.sprite.Group()
        pg.display.set_caption("sideways shootber")
        self.aliens=pg.sprite.Group()
        self._create_fleet()
        self.stats=Stats(self)
        self.play_button=Button(self,"Play")
        self.sb=SB(self)
        self.ships=pg.sprite.Group()


    def run_game(self):
        """the main loop"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _create_ships(self):
        """create ships at the top left side of the score"""
        for ship_number in range(self.settings.ship_limit):
            ship=Ship(self)
            ship_width=ship.rect.width
            ship.rect.x=ship_width+ship_width*ship_number
            ship.rect.y=0
            self.ships.add(ship)


    def _check_events(self):
        """check the keypresses and releases"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._close_game()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.ship.moving_up=False
                elif event.key == pg.K_DOWN:
                    self.ship.moving_down=False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos=pg.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self,mouse_pos):
        """respond when the player clicks Play"""
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        """start the game"""
        self.stats.game_active=True  
        self.stats.reset_stats()
        self.aliens.empty()
        self.bullets.empty()
        self.ship.center_ship()
        self._create_fleet()
        self.settings.initialize_dynamic_settings()
        self.sb.prep_score()
        self._create_ships()
        self.sb.level=0
        self.sb.prep_level()
        pg.mixer.music.load("sounds/music.ogg")
        pg.mixer.music.play(-1)
    
    def _check_keydown_events(self,event):
        """respond to keys pressed by the player"""
        if event.key == pg.K_UP:
            self.ship.moving_up=True
        elif event.key == pg.K_DOWN:
            self.ship.moving_down=True
        elif event.key == pg.K_q:
            self._close_game()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _create_fleet(self):
        """create a fleet of aliens"""
        alien=Alien(self)
        ship_width=self.ship.rect.width
        alien_width,alien_height=alien.rect.size
        num=randint(0,2)
        #count the space available for aliens.
        available_space_y=self.settings.screen_height - (num*alien_height)
        available_space_x=self.settings.screen_width - (
            2*alien_width) - ship_width
        #count the number of rows of aliens.
        num2=randint(0,5)
        num3=randint(2,7)
        number_aliens=available_space_y // (2*alien_height)
        number_rows=available_space_x // (2*alien_width)
        number_aliens-=num2
        number_rows-=num3
        for number_row in range(number_rows):
            for number_alien in range(number_aliens):
                self._create_alien(number_row,number_alien)


    def _create_alien(self,number_row,number_alien):
        """add an alien to the fleet of aliens"""
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        alien.rect.x=self.settings.screen_width - alien_width - (
            2*alien_width * number_row)
        alien.rect.y=alien_height + (2*alien_height*number_alien)
        self.aliens.add(alien)
        

    def _update_aliens(self):
        """update the posititons of aliens based on the direction flag"""
        for alien in self.aliens.sprites():
            alien.rect.y+=(
                self.settings.aliens_speed2 * self.settings.aliens_direction)
            if alien.rect.left <=0:
                self._ship_hit()
        collisions=pg.sprite.spritecollideany(self.ship,self.aliens)
        if collisions:
            self._ship_hit()
        self._check_aliens_edges()
        if not self.ships:
            self.stats.game_active=False

    def _ship_hit(self):
        """respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            #decrement the number of the remained ships.
            self.stats.ships_left-=1
            #remove any bullets and aliens from the screen.
            self.bullets.empty()
            self.aliens.empty()
            #center the ship.
            self.ship.center_ship()
            #create a new fleet of aliens.
            self._create_fleet()
            #remove a ship.
            for ship in self.ships.copy():
                self.ships.remove(ship)
                break
            #pause.
            sleep(0.5)
        else: 
            self.stats.game_active = False

    
    def _check_aliens_edges(self):
        """check if the aliens hit the edge of the screen"""
        opposite=False
        drop=False
        for alien in self.aliens.sprites():
            if alien.check_edges():
                opposite=True
                drop=True
        if drop:
            for alien in self.aliens.sprites():
                alien.rect.x-=self.settings.drop_speed
        if opposite:
            self.settings.aliens_direction*=-1
                    

    def _fire_bullet(self):
        """add a bullet to the group of bullets"""
        if len(self.bullets) < self.settings.bullets_limit:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)


    def _update_screen(self):
        """update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.update()
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        self.sb.draw_score()
        self.ships.draw(self.screen)
        pg.display.flip()


    def _update_bullets(self):
        """update the position of bullets"""
        self.bullets.update()
        #get rid of the disappeared bullets.
        for bullet in self.bullets.copy():   
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        #check for collisions and remove the alien and bullet that collided.
        collisions=pg.sprite.groupcollide(self.bullets,self.aliens,True,True)
        for aliens in collisions.values():
            self.settings.score+=len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens.sprites():
            self.bullets.empty()
            self._create_fleet()
            self.settings.speed_up()
            self.sb.level+=1
            self.sb.prep_level()

    def _close_game(self):
        """close the game"""
        saved_high_score=self.sb.get_saved_high_score()
        if self.sb.high_score > saved_high_score:
            with open("high_score2.json",'w') as file:
                json.dump(self.sb.high_score,file)
        sys.exit()



if __name__=='__main__':
    game=Shooter()
    game.run_game()
