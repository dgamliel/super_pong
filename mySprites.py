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
    #get center x positon
    def get_x(self):
        return self.rect.centerx
    #get center y position
    def get_y(self):
        return self.rect.centery

    #Sets the x and y position of the ball
    def set_x(self):
        self.rect.centerx = self.rect.centerx + self.dx
    def set_y(self):
        self.rect.centery = self.rect.centery + self.dy

    #Sets the dx and dy (speed) and direction of the ball
    def set_DX(self,speed):
        self.dx = speed
    def set_DY(self,speed):
        self.dy = speed
    def get_DX(self):
    	return self.dx
    def get_DY(self):
    	return self.dy

    #Checks if ball will be off screen and reverses dx or dy (direction and speed) if so
    def check_edge(self):
        #ball goes off x axis
        if(self.rect.centerx > 720 or self.rect.centerx < 0):
            self.dx = -self.dx
        #ball goes off y axis
        elif(self.rect.centery > 480 or self.rect.centery <0):
            self.dy = -self.dy
    #updates the balls position based on speed and checks for edge collision
    def update(self):
    	self.set_x()
    	self.set_y()
    	self.check_edge()

class PlayerBar(pygame.sprite.Sprite):

    dy = 0

    def __init__(self,x,y,dy):
    	#Initiates Sprite super
        pygame.sprite.Sprite.__init__(self)
        #Loads in png and converts to rectangle
        self.image = pygame.image.load('PlayerBar.png').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.dy = dy
    #get center x position
    def get_x(self):
        return self.rect.centerx
    #get center y position
    def get_y(self):
        return self.rect.centery

    #Sets the y position of the ball
    def set_y(self):
        self.rect.centery = self.rect.centery + self.dy #this is how position changes based on speed

    #Sets the dy (speed) and direction of the ball
    def set_DY(self,speed):
        self.dy = speed
    #Checks for edge of playable field
    def check_edge(self):
        #bar moves off y axis
        if(self.rect.centery >= 480 or self.rect.centery <= 0):
            self.dy = 0
            return True
        return False
    #updates the PlayerBar position, should be used before drawing
    def update(self):
        if(not self.check_edge()): #if it is not at edge of game field, update position
            self.set_y()
