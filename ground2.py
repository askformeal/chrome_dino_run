import pygame

class Ground2:
    # this class represent the ground.
    def __init__(self,main):
        #the parament 'main' is the main class of the game. 
        self.main = main
        self.screen = main.screen

        self.sprite = pygame.image.load('sprite.bmp')
        # the rect is the body of the ground, and image make it visible
        self.rect = pygame.Rect((1204,main.height-10),(main.width,10))
        self.image = pygame.Surface((1204,10))
        self.image.blit(self.sprite,(0,0),(2,58,1204,10))

        #x and y is also needed too.
        self.x,self.y = self.rect.x,self.rect.y

    def update(self):
        self.screen.blit(self.image,(self.x,self.y))
        if self.main.started:
            self.rect.x = self.x
            self.rect.y = self.y
            # get the part of dino
            #the 678,3 represent the topleft corner of the dino image,
            #and the 43,50 represent the widght and height of the image.
            
        
       
            self.screen.blit(self.image,(self.x,self.y))
            self.x -= self.main.speed
            if self.x <= 0:
                self.x = 1204