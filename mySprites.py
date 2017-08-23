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

class GameBall(pygame.sprite.Sprite):

    dx = 0 #direction & speed of ball along x axis
    dy = 0 #direction & speed of ball along y axis

    def __init__(self,x,y,dx,dy):
        #Initiates Sprite super
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('GameBall.png').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.dx = dx
        self.dy = dy

    def get_x():
        return self.rect.centerx

    def get_y():
        return self.rect.centery

    #Sets the x and y position of the ball
    def set_x():
        self.rect.centerx = self.rect.centerx + dx
    def set_y():
        self.rect.centery = self.rect.centery + dy

    #Sets the dx and dy (speed) and direction of the ball
    def set_DX(speed):
        dx = speed
    def set_DY(speed):
        dy = speed

    #Checks if ball will be off screen and reverses dx or dy (direction and speed) if so
    def check_edge():
        #ball goes off x axis
        if(self.rect.centerx > 720 or self.rect.centerx < 0):
            dx = -dx
        #ball goes off y axis
        elif(self.rect.centery > 480 or self.rect.centery <0):
            dy = -dy

    def hit_check():
        if((PlayerBar.get_x() - get_x() < dx) and 
            (PlayerBar.get_y() + 2 > get_y() & PlayerBar.get_y() - 2 < get_y())):
            

    def update():
        set_x()
        set_y()
        check_edge()

class PlayerBar(pygame.speed.Sprite):

    dx = 0
    dy = 0

    def __init__(self,x,y,dy):

        pygame.speed.Sprite.__init__(self)

        self.image = pygame.image.load('PlayerBar.png').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.dy = dy

    def get_x():
        return self.rect.centerx

    def get_y():
        return self.rect.centery

    #Sets the y position of the ball
    def set_y():
        self.rect.centery = self.rect.centery + dy

    #Sets the dy (speed) and direction of the ball
    def set_DY(speed):
        dy = speed

    def check_edge():
        #bar moves off y axis
        if(self.rect.centery >= 480 or self.rect.centery <= 0):
            dy = 0
            return True
        return False

    def update():
        if(!check_edge()):
            set_y()
