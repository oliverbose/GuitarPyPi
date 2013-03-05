#!/usr/bin/python
import random, sys, time, math, pygame
from pygame.locals import *



def main():
    global guitar, chordsOpen, chordsMuted, chordToPlay

    # we need to reduce the default buffer size to have low latency
    pygame.mixer.pre_init(44100,-16,1,512)
    pygame.init()
    pygame.joystick.init()
    guitar = pygame.joystick.Joystick(0)
    guitar.init()

    chordsOpen = { 0: pygame.mixer.Sound("../audio/E-open.ogg"),\
                 1: pygame.mixer.Sound("../audio/G-open.ogg"),\
                 2: pygame.mixer.Sound("../audio/A-open.ogg"),\
                 3: pygame.mixer.Sound("../audio/C-open.ogg"),\
                 4: pygame.mixer.Sound("../audio/D-open.ogg"),\
                 5: pygame.mixer.Sound("../audio/E8-open.ogg")}

    chordsMuted = {0: pygame.mixer.Sound("../audio/E-muted.ogg"),\
                 1: pygame.mixer.Sound("../audio/G-muted.ogg"),\
                 2: pygame.mixer.Sound("../audio/A-muted.ogg"),\
                 3: pygame.mixer.Sound("../audio/C-muted.ogg"),\
                 4: pygame.mixer.Sound("../audio/D-muted.ogg"),\
                 5: pygame.mixer.Sound("../audio/E8-muted.ogg")}
                 
    chordToPlay = 0

    while True:
        fist()


def fist():
    global guitar, chordsOpen, chordsMuted, chordToPlay
    
    int 
    for event in pygame.event.get(): # event handling loop
        if event.type == JOYHATMOTION:
#            print"GotEvent  JOYHATMOTION", event.value
            if event.value == (0,0):
                stopAll()
            elif event.value == (0,-1):
                chordsOpen[chordToPlay].play(0,0,0)
            elif event.value == (0,1):
                chordsMuted[chordToPlay].play(0,0,0)

        elif event.type == JOYBUTTONDOWN:
 #           print("GotEvent  JOYBUTTONDOWN")
            if event.button == 0:
                chordToPlay = 1
            elif event.button == 1:
                chordToPlay = 2
            elif event.button == 2:
                chordToPlay = 4
            elif event.button == 3:
                chordToPlay = 3
            elif event.button == 4:
                chordToPlay = 5
        elif event.type == JOYBUTTONUP:
  #          print("GotEvent  JOYBUTTONUP")
            if noButtonPresed() :
                chordToPlay = 0


def noButtonPresed():
    global guitar
    status =  ( not guitar.get_button(0) \
            	and not guitar.get_button(1) \
    		and not guitar.get_button(2) \
		and not guitar.get_button(3) \
		and not guitar.get_button(4))
    return status

def stopAll():
    pygame.mixer.stop()


if __name__ == '__main__':
    main()
