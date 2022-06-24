import pygame as pg
from random import random
from random import randint
import sys
import json
from time import sleep

from shooter_settings import Settings
from ship3 import Ship
from bullet2 import Bullet
from alien2 import Alien
from button import Button
from score_board3 import ScoreBoard as SB
from sw_shooter_stats import Stats

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
        alien=Alien(self)
        self.x=alien.rect.x
        self.play_button=Button(self,"Play")
        self.sb=SB(self)
        self.stats=Stats(self)
        self.ships=pg.sprite.Group()


    def run_game(self):
        """the main loop"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._create_alien()
                self._update_aliens()
            self._update_screen()


    def _check_events(self):
        """check the keypresses and releases"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._close_game()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pg.MOUSEBUTTONDOWN:
                mouse_pos=pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.ship.moving_up=False
                elif event.key == pg.K_DOWN:
                    self.ship.moving_down=False

    def _close_game(self):
        """close the game"""
        saved_high_score=self.sb.get_saved_high_score()
        if self.sb.high_score > saved_high_score:
            with open("high_score3.json",'w') as file:
                json.dump(self.sb.high_score,file)
        sys.exit()

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
        self.settings.initialize_dynamic_settings()
        self.sb.prep_score()
        self._create_ships()
        self.sb.level=0
        self.sb.prep_level()
        pg.mixer.music.load("sounds/music.ogg")
        pg.mixer.music.play(-1)

    def _create_ships(self):
        """create ships at the top left side of the score"""
        for ship_number in range(self.settings.ship_limit):
            ship=Ship(self)
            ship_width=ship.rect.width
            ship.rect.x=ship_width+ship_width*ship_number
            ship.rect.y=0
            self.ships.add(ship)

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
        elif event.key == pg.K_p:
            self._start_game()

    def _create_alien(self):
        """add an alien to the fleet of aliens"""
        if random() < self.settings.frequency:
            alien=Alien(self)
            self.aliens.add(alien)


    def _update_aliens(self):
        """update the positions of aliens"""
        self.aliens.update()
        collisions=pg.sprite.spritecollideany(self.ship,self.aliens)
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._ship_hit()
        if collisions:
            self._ship_hit()
        if not self.ships.sprites():
            self.stats.game_active=False
            pg.mixer.music.stop()

    def _ship_hit(self):
        """respond when the ship gets hit or 
        when an alien reaches the edge of the screen"""
        for ship in self.ships.copy():
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            self.ships.remove(ship)
            sleep(0.5)
            break

    def _fire_bullet(self):
        """add a bullet to the group of bullets"""
        if len(self.bullets) < self.settings.bullets_limit:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
            pg.mixer.Sound("sounds/fire.wav").play()


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
            pg.mixer.Sound("sounds/explosion.flac").play()
            self.sb.prep_score()
            self.sb.check_high_score()
            if self.settings.score%10==0:
                self.settings.speed_up()
                self.sb.level+=1
                self.sb.prep_level()
                pg.mixer.Sound("sounds/new_level.ogg").play()
        



if __name__=='__main__':
    game=Shooter()
    game.run_game()
