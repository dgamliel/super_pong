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

        self.rect = self.image.get_rect()
        self.image.fill((0,0,0))
        print(self.rect)