class Settings():
    """settings for sideways shooter game"""
    def __init__(self):
        """initialize the settings of the game"""
        #screen settings
        self.screen_width=1200
        self.screen_height=650
        self.bg_color=(230,230,230)
        
        #ship settings
        
        self.ship_limit=3
        
        #bullets settings
        self.bullet_height=6
        self.bullet_width=30
        
        self.bullet_color=(200,0,0)
        self.bullets_limit=4

       
        #the direction flag where 1 means down and -1 means up.
        self.aliens_direction=1
        self.drop_speed=20
        #the frequency of the formation of new aliens.
        self.frequency=0.0055
        #how quickly the game speeds up.
        self.speed_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change during the game"""
        #aliens settings
        self.aliens_speed=2
        self.aliens_speed2=5
        self.aliens_speed3=0.7
        self.bullet_speed=2
        self.bullet_speed2=1.4
        self.ship_speed=1.7
        self.ship_speed2=1.4
        self.ship_speed3=1
        self.alien_points=50
        self.score=0


    def speed_up(self):
        """increase the spead of the game"""
        self.aliens_speed*=self.speed_scale
        self.bullet_speed*=self.speed_scale
        self.ship_speed*=self.speed_scale