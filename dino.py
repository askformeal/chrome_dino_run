import pygame

class Dino:
    # the dinosaur
    def __init__(self,main):
        self.main = main
        self.screen = main.screen
        self.sprite = pygame.image.load('sprite.bmp')
        self.x,self.y = self.main.width/24,self.main.height-60
        self.rect = pygame.Rect(self.x,self.y,43,50)
        
        # get the part of dino
        #the 678,3 represent the topleft corner of the dino image,
        #and the 43,50 represent the widght and height of the image.
        self.image_start = pygame.Surface((43,50))
        self.image_start.blit(self.sprite,(0,0),(678,3,43,50))

        self.image_run1 = pygame.Surface((43,50))
        self.image_run1.blit(self.sprite,(0,0),(766,3,43,50))
        
        self.image_run2 = pygame.Surface((43,50))
        self.image_run2.blit(self.sprite,(0,0),(810,3,43,50))

        self.current_image = self.image_start
        

    def change_image(self):
        if self.current_image == self.image_run1:
            self.current_image = self.image_run2
        else:
            self.current_image = self.image_run1

    def update_image(self):
        # everything about image
        if self.main.started and self.main.timer%0.2 == 0:
            self.change_image()
            
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.update_image()
        
        self.screen.blit(self.current_image,(self.x,self.y))