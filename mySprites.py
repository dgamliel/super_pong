import pygame

class Cursor(pygame.sprite.Sprite):

    def __init__(self):
        #Calls the constructor of the parent class
        pygame.sprite.Sprite.__init__(self)
        try:
            self.image = pygame.image.load('cursor.png').convert_alpha()
        except:
            print ('Image *CURSOR.PNG* failed to load')
        self.rect = self.image.get_rect()

    def rect_return(self):
        return self.rect

