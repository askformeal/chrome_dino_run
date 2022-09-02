from time import sleep
import pygame
from pygame.sprite import Sprite
from random import choice

from copper import cop

class Cactu(Sprite):
    #a SINGLE cactu
    def __init__(self,main):
        super().__init__()
        self.screen = main.screen
        self.main = main
        image1 = cop((229,3),(16,34))
        image2 = cop((246,3),(16,34))
        image3 = cop((264,3),(16,34))
        image4 = cop((280,3),(16,34))
        image5 = cop((297,3),(16,14))
        image6 = cop((314,3),(16,14))
        image7 = cop((333,3),(24,47))
        image8 = cop((358,3),(24,47))
        image9 = cop((383,3),(24,47))
        image10 = cop((408,3),(24,47))
        image11 = cop((432,3),(50,47))
        self.images = [image1,image2,image3,image4,image5,image6,image7,
            image8,image9,image10,image11]
        self.image = choice(self.images)
        self.rect = self.image.get_rect()
        # only the cactu's x was needed to be changed
        self.x = self.main.width + self.rect.width
        #self.x = 100
        self.rect.y = self.main.height - (self.rect.height+5)


    

    def update(self):
        self.rect.x = self.x
        if self.main.started:
            self.screen.blit(self.image,(self.x,self.rect.y))
            self.x -= self.main.speed
