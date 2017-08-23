import pygame

class Cursor(pygame.sprite.Sprite):

    def __init__(self, x=175, y=380):
        #Calls the constructor of the parent class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('cursor.png').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def get_x(self):
        return self.rect.centerx

    def get_y(self):
        return self.rect.centery

class CursorCover(pygame.sprite.Sprite):
    
    def __init__(self, cursor_obj):
        #inits the super class
        pygame.sprite.Sprite.__init__(self)

        #Creates the image of the block exactly the size of the cursor
        x = cursor_obj.get_x()
        y = cursor_obj.get_y()

        self.image = pygame.Surface([x,y])

        #updates the rect private member var 
        self.rect = self.image.get_rect()

        #sets the center of the rect at coordiantes x and y+100
        self.rect.centerx = x                                      #sets center of block at center of text
        self.rect.centery = y + 100                                #sets center of y 100 pixels below text

        self.image.fill((0,0,0)) #Fills image with color black