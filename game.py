import pygame
import time
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption('Initial Pygame')

    #fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    #Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Nigger game", 1, (10,10,10,))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    #Blit everything to the screen
    screen.blit(background, (0,0))
    pygame.display.flip()

    #Event loop

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == '__main__': main()