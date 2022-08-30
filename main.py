import pygame
import sys
import time

from dino import Dino
from ground1 import Ground1
from ground2 import Ground2

HEIGHT = 350
WIDTH = 1204
BG_COLOR = (0,0,0)
SPEED = 1

class Main:
    # class of the game
    def __init__(self):
        pygame.init()
        
        self.width,self.height = WIDTH,HEIGHT
        # ^^^ this might look useless, but so the other files(like ground.py)
        #can access the width and height of the screen, too
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption(f"---|Chrome Dino Run|---")
        #pygame can work with most of the image types, but the *.bmp is the 
        #best.
        self.sprite = pygame.image.load('sprite.bmp')

        self.speed = SPEED

        self.started = False

        #the start time of the game(since the epoch)
        self.start_time = time.time()

        #the main timer of the game
        self.timer = 0

        #from here is the object of everthing in the game.
        # the ground :)
        self.ground1 = Ground1(self)
        # the another ground
        self.ground2 = Ground2(self)
        # the dino
        self.dino = Dino(self)
        
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
        elif event == pygame.K_t:
            #the test key,delete later
            print(f'this is the timer: {self.timer}')
    
    def _check_keyup(self,event):
        pass

    def update_timer(self):
        #update the time
        self.timer = round(time.time() - self.start_time,1)

    def update(self):
        bg_color = BG_COLOR
        self.screen.fill(bg_color)
        self.update_timer()

        self.dino.update()
        self.ground1.update()
        self.ground2.update()

        pygame.display.flip()
        
        
    def run_game(self):
        while True:
            self.update()
            self.check()

if __name__ == '__main__':
    main = Main()
    main.run_game()
