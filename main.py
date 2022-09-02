from random import randint
import pygame
import sys
import time
import json

from dino import Dino
from ground1 import Ground1
from ground2 import Ground2
from cactu import Cactu

#read settings from settings.json
with open('setting.json') as f:
    settings = json.load(f)


if settings['dino_max_jump'] <= 60:
    print('''WARNING: variable 'DINO_MAX_JUMP' has to be bigger than 60 if you want to make the dino jump any height. press Eenter to continue.''')
    temp = input()
if len(str(settings['dino_run_speed'])) > 3:
    raise Exception(" variabkeDINO_RUN_SPEED's ndigit is too long")


class Main:
    # class of the game
    def __init__(self):
        pygame.init()

        self.dino_max_jump = settings['dino_max_jump']
        self.dino_run_speed = settings['dino_run_speed']
        self.width,self.height = settings['width'],settings['height']
        self.jump_speed = settings['jump_speed']

        # ^^^ this might look useless, but so the other files(like ground.py)
        #can access the width and height of the screen, too
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption(f"---|Chrome Dino Run|---")
        #pygame can work with most of the image types, but the *.bmp is the 
        #best.
        self.sprite = pygame.image.load('sprite.bmp')

        self.speed = settings['speed']

        self.distance = 0

        self.started = False

        #the start time of the game(since the epoch)
        self.start_time = time.time()

        #the main timer of the game
        self.timer = 0
        self.run_counter = 0
        #seperate of run between spawn of cactus
        self.current_seperate = 0

        #from here is the object of everthing in the game.
        # the ground :)
        self.ground1 = Ground1(self)
        # the another ground
        self.ground2 = Ground2(self)
        # the dino
        self.dino = Dino(self)
        
        #easter egg
        self.test_cactu = Cactu(self)

        # cautus
        self.cautus = pygame.sprite.Group()


        
    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event.key)                   
            elif event.type == pygame.KEYUP:
                self._check_keyup(event.key)

    def _check_keydown(self,event):
        if event == pygame.K_ESCAPE:
            sys.exit()
        elif event == pygame.K_SPACE:
            
            if not self.started:
                self.started = True
            elif self.dino.jump_state == 0:
                self.dino.jump_state = 1
        elif event == pygame.K_t:
            #the test key,delete later
            self.cautus.add(Cactu(self))
 
    
    def _check_keyup(self,event):
        pass

    def update_timer(self):
        #update the time
        self.timer = round(time.time() - self.start_time,1)
        self.run_counter += 1
    
    def update_cactus(self):
        if self.distance > 10000:
            self.cautus.update()
            self.current_seperate = randint(9999,150000)
            if self.run_counter%1090 == 0:
                self.cautus.add(Cactu(self))
            for cactu in self.cautus:
                if cactu.x < -cactu.rect.width:
                    self.cautus.remove(cactu)
        
        if pygame.sprite.spritecollideany(self.dino, self.cautus):
            sys.exit()

    def update_speed(self):
        # self.speed += 0.000000000000001
        self.distance += self.speed

    def update(self):
        bg_color = tuple(settings['bg_color'])
        self.screen.fill(bg_color)
        self.update_timer()
        self.update_speed()

        self.dino.update()
        self.ground1.update()
        self.ground2.update()
        #self.test_cactu.update()
        self.update_cactus()

        pygame.display.flip()
        
        
    def run_game(self):
        while True:
            self.update()
            self.check()

if __name__ == '__main__':
    main = Main()
    main.run_game()
