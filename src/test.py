#!/usr/bin/python
import random, sys, time, math, pygame
from pygame.locals import *



def main():
    global guitar, playing, ruelpser1, ruelpser2, ruelpserToPlay

    playing = False
    # we need to reduce the default buffer size to have low latency
    pygame.mixer.pre_init(44100,-16,2,768)
    pygame.init()
    pygame.joystick.init()
    guitar = pygame.joystick.Joystick(0)
    guitar.init()
    ruelpser1 = pygame.mixer.Sound("../audio/ruelps.ogg")
    ruelpser2 = pygame.mixer.Sound("../audio/ruelps2.ogg")
    ruelpserToPlay = ruelpser1
    while True:
        fist()


def fist():
    global guitar, playing, ruelpser1, ruelpser2, ruelpserToPlay
    
    #pygame.mixer.music.play()
    #print(pygame.joystick.get_count())
    

    #i = 0
    #while i < guitar.get_numbuttons():
    #    print "A%d:%d " %(i,guitar.get_button(i))
    #    i = i+1
    for event in pygame.event.get(): # event handling loop
        if event.type == JOYHATMOTION:
            if playing:
                ruelpserToPlay.stop()
                playing = False
            else:
                ruelpserToPlay.play(0,0,0)
                playing = True
        elif event.type == JOYBUTTONDOWN:
            if event.button == 0:
                ruelpserToPlay = ruelpser1
            elif event.button == 1:
                ruelpserToPlay = ruelpser2
        elif event.type == JOYBUTTONUP:
            if event.button == 0:
                ruelpser1.stop()
            elif event.button == 1:
                ruelpser2.stop()


    

if __name__ == '__main__':
    main()
