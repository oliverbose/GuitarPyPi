#!/usr/bin/python
import random, sys, time, math, pygame
from pygame.locals import *

numChordButtons = 5

def main():
    global guitar, chordsOpen, chordsMuted, chordToPlay
    print "Initialization start..."
    # we need to reduce the default buffer size to have low latency ~50ms at 300
    pygame.mixer.pre_init(44100,-16,1,300)
    pygame.init()
    pygame.joystick.init()
    pygame.event.set_blocked(JOYAXISMOTION)

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
    print "Initialization complete"
    while True:
        fist()


def fist():
    global guitar, chordsOpen, chordsMuted
    

    event = pygame.event.wait()
    #print "GotEvent  " + pygame.event.event_name(event.type)
    if event.type == JOYHATMOTION:
        if event.value == (0,0):
            stopAll()
        elif event.value == (0,-1):
            playOpen()
        elif event.value == (0,1):
            playMuted()

def stopAll():
    pygame.mixer.stop()

def playOpen():
    global chordsOpen
    chordsOpen[getActiveChordButton()].play()

def playMuted():
    global chordsMuted
    chordsMuted[getActiveChordButton()].play()
    
def getActiveChordButton():
    global guitar
    buttonId = 0
    while buttonId < numChordButtons:
        if (guitar.get_button(buttonId)):
            if (buttonId == 2):
                return buttonId + 2
            if (buttonId == 3):
                return buttonId
            return buttonId + 1
        buttonId = buttonId + 1
    return 0

if __name__ == '__main__':
    main()
