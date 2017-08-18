#Daniel Gamliel
#Super pong v0.1

try:
    import os
    import sys
    import pygame
    import mySprites #Sprite module that I wrote
    import math
    import random
    from pygame.locals import *
    import time
except ImportError:
    print ('Unable to locate libarary')
    sys.exit(2)

def loading_img(name):
    pwd = os.cwd()
    fullname = os.path.join(pwd, name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except (pygame.error, message):
        print ('Cannot load image from: ', fullname)
        raise (SystemExit, message)
    return image, image.get_rect()

def start_sound():
    try:
        pwd = os.cwd()
        fullname = os.path.join(pwd, 'audio')
    except:
        print('Failed to load audio from: ', fullname)
        raise (SystemExit)

#takes a pygame.display (screen) object input
def setup_screen(screen_obj):

    #clears screen
    screen_obj.fill((0,0,0))
    pygame.display.flip()

    #Creates text at top
    choiceText = pygame.font.SysFont('robotocondensed', 32, bold=True)
    choiceTextRend = choiceText.render('Choose player count!', True, (250,250,250))
    choiceTextRect = choiceTextRend.get_rect()
    choiceTextRect.centerx = screen_obj.get_rect().centerx
    choiceTextRect.centery = 80

    #Text for One player
    onePlayer = pygame.font.SysFont('robotocondensed', 42)
    onePlayerRend = onePlayer.render('ONE PLAYER', True, (250,250,250))

    #Text for Two players
    twoPlayer = pygame.font.SysFont('robotocondensed', 42)
    twoPlayerRend = twoPlayer.render('TWO PLAYERS', True, (250,250,250))

    #loads cursor
    cursor = mySprites.Cursor()

    #Blits everything to screen
    screen_obj.blit(onePlayerRend, (80, 240))
    screen_obj.blit(twoPlayerRend, (430, 240))
    screen_obj.blit(cursor.image, cursor.rect)
    screen_obj.blit(choiceTextRend, choiceTextRect)
    pygame.display.flip()

#Main function

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
    mainText = pygame.font.SysFont('robotocondensed', 32, bold=True)     #creates font object with font 'Roboto Condensed'
    mainTextDisplay = mainText.render('Super Pong', True, (250,250,250)) #Renders font (will not show until blitted) with RGB (250,250,250)
    mainTextPos = mainTextDisplay.get_rect()                             #Returns a rect object of mainTextDisplay stored in mainTextPos
    mainTextPos.centerx = background.get_rect().centerx                  #centers main text at 720/2p == 360p  
    mainTextPos.centery = background.get_rect().centery                  #centers main text at 480/2p == 240p

    #Subtext display
    subText = pygame.font.SysFont('robotocondensed', 24)
    subText = subText.render('Press any button to play!', True, (230, 230, 230))
    subTextPos = subText.get_rect()
    subTextPos.centerx = background.get_rect().centerx
    subTextPos.y = 360

    #Blits everything to the screen
    background.blit(mainTextDisplay, mainTextPos) #Blits mainText on background
    background.blit(subText, subTextPos)          #Blits subText on background (x-centered, y-360p)
    screen.blit(background,(0,0))                 #Blits background to screen
    pygame.display.flip()                         #Refreshes screen to display blitting

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                setup_screen(screen)
                

if __name__ == '__main__': main()