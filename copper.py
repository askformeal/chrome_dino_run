import pygame
#this a function used to cop image in pygame
def cop(top_left=(),size=(),my_sprite='sprite.bmp'):
    sprite = pygame.image.load(my_sprite)
    surface = pygame.Surface(size)
    temp_tuple = (top_left[0],top_left[1],size[0],size[1])
    surface.blit(sprite,(0,0),temp_tuple)
    return surface