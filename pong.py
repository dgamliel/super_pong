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

    #Blits everything to screen
    screen_obj.blit(onePlayerRend, (80, 240))
    screen_obj.blit(twoPlayerRend, (430, 240))
    #screen_obj.blit(cursor.image, cursor.rect)
    screen_obj.blit(choiceTextRend, choiceTextRect)
    pygame.display.flip()

def cursor_blit(screen_obj, event):

    cursorPlacement = 0

    #Creates cursor object and cursor Cover object
    cursor = mySprites.Cursor() #Constructor takes default x,y coord to be placed under onePlayerText

    #Creates group to manage cursor covers
    cursorCoverGroup = pygame.sprite.Group()

    #Creates group to manage cursors
    cursorGroup = pygame.sprite.Group()
    cursorGroup.add(cursor)

    #displays cursor Spite to screen
    cursorGroup.draw(screen_obj)
    pygame.display.flip()

    if event.key == K_RIGHT:
        cursorPlacement+=1
        if abs(cursorPlacement) == 1 or abs(cursorPlacement) % 2 is not 0:

            #creates block object and removes cursor from cursorgroup
            block = mySprites.CursorCover(cursor)
            cursorGroup.remove(cursor)

            #creates new cursor underneath player 2 texts and adds to group
            left_cursor = mySprites.Cursor(540,380)
            cursorGroup.add(left_cursor)
            cursorCoverGroup.add(block)
            
            #draws and updates screen
            cursorGroup.draw(screen_obj)
            cursorCoverGroup.draw(screen_obj)
            cursorGroup.update()
            pygame.display.flip()

def game_screen(screen_obj,event):
    screen_obj.fill((0,0,0))
    #Creates all Objects in game with set positions
    ball = mySprites.GameBall(300,200,-10,0) # x , y , dx , dy
    playerBar = mySprites.PlayerBar(540,240,0) # x , y , dy
    clock = pygame.time.Clock()

    #Sets up groups for objects and player objects and draws them to screen
    gameObjectGroup = pygame.sprite.Group()
    playerObjectGroup = pygame.sprite.Group()
    gameObjectGroup.add(ball)
    playerObjectGroup.add(playerBar)
    gameObjectGroup.update()
    playerObjectGroup.update()
    gameObjectGroup.draw(screen_obj)
    playerObjectGroup.draw(screen_obj)
    pygame.display.flip()
    #MAIN GAME LOOP
    while True:
            pygame.time.wait(34) #FPS in milliseconds (wait 34 milliseconds between frames)
            screen_obj.fill((0,0,0)) #wipe screen clean before repainting objects 
            hit_check(playerBar,ball) #check for collisions
            gameObjectGroup.update()
            gameObjectGroup.draw(screen_obj) #draw GameBall
            playerObjectGroup.draw(screen_obj) #draw PlayerBar
            pygame.display.flip()
            #awaits key strokes to move PlayerBar
            for event in pygame.event.get():
            	#downward movement
               if event.type == pygame.KEYDOWN and event.key == K_DOWN:
                    playerBar.set_DY(-30)
                    playerObjectGroup.update()
                    playerObjectGroup.draw(screen_obj)
                #upward movement
               elif event.type == pygame.KEYDOWN and event.key == K_UP:
                    playerBar.set_DY(30)
                    playerObjectGroup.update()
                    playerObjectGroup.draw(screen_obj)

#checks if GameBall and PlayerBar will collide in the next frame, if so, changes direction of ball
def hit_check(PlayerBar,GameBall):
    playerBarRange = [PlayerBar.rect.top, PlayerBar.rect.bottom]
    ballRange = [GameBall.rect.top, GameBall.rect.bottom]



    if(PlayerBar.get_x() - GameBall.get_x() < GameBall.dx) and (PlayerBar.get_y() + 50 > GameBall.get_y() and PlayerBar.get_y() - 50 < GameBall.get_y()):
        GameBall.set_DX(-GameBall.get_DX())
        return True
    

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
                cursor_blit(screen, event)
                if event.key == K_RETURN:

                    game_screen(screen,event)


   

if __name__ == '__main__': main()
