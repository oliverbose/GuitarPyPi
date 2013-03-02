#!/usr/bin/python
import random, sys, time, math, pygame
from pygame.locals import *



def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

    pygame.init()
    pygame.joystick.init()
    #FPSCLOCK = pygame.time.Clock()
    
    # while True:
    runGame()


def runGame():
    pygame.mixer.music.load("../audio/ruelps.ogg")
    
    pygame.mixer.music.play()
    #print(pygame.joystick.get_count())
    


if __name__ == '__main__':
    main()
