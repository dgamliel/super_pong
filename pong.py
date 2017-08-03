#Daniel Gamliel
#Super pong v0.1

try:
    import os
    import sys
    import pygame
    import math
    import random
    from pygame.locals import *
    import time
except (ImportError, err):
    print ('Unable to locate libarary :%s' %(err))
    sys.exit(2)

def loading_img(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except (pygame.error, message):
        print ('Cannot load image: ', fullname)
        raise (SystemExit, message)
    return image, image.get_rect()

def start_sound():
    try:
        pygame.mixer.play()
    except:
        pass

def setup_screen():
    return
    

def main():
    pygame.init() #initalizes a pygame object

    #Initializes window
    screen = pygame.display.set_mode((720,480)) #creates a window for the pygame object to interact with && sets dimension of 720x480p
    pygame.display.set_caption('Super Pong')

    #Sets background
    background = pygame.Surface(screen.get_size()) #create a background that has the size of the screen
    background = background.convert()              #allows for faster blitting
    background.fill((0,0,0))                       #creates a black background

    #Main Text display
    mainText = pygame.font.SysFont('robotocondensed', 32, bold=True) #creates font object
    mainTextDisplay = mainText.render('Super Pong', True, (250,250,250))          #Renders font (will not show until blitted)
    mainTextPos = mainTextDisplay.get_rect()
    mainTextPos.centerx = background.get_rect().centerx
    mainTextPos.centery = background.get_rect().centery

    #Subtext display
    subText = pygame.font.SysFont('robotocondensed', 24)
    subText = subText.render('Press any button to play!', True, (230, 230, 230))
    subTextPos = subText.get_rect()
    subTextPos.centerx = background.get_rect().centerx
    subTextPos.y = 360

    background.blit(mainTextDisplay, mainTextPos) #Blits mainText on background
    background.blit(subText, subTextPos)  #Blits subText on background (x-centered, y-360p)
    screen.blit(background,(0,0))                 #Blits background to screen
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                #setup_screen()
                return

if __name__ == '__main__': main()