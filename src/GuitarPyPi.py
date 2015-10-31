#!/usr/bin/python
import pygame
import Config
from pprint import pprint
from pygame.locals import *

NO_BUTTON_CHORD = 0

def main():
    global guitar, chordsOpen, chordsMuted, chordsToPlay, playing, playOpen, songs, currentSong

    print "Initialization start..."
    
	
	# Add some Halloween Eye-Candy    
	print "              (                                ("
	print "                )           )        (                   )"
	print "              (                       )      )            .---."
	print "          )              (     .-\"\"-.       (        (   /     \\"
	print "         ( .-\"\"-.  (      )   / _  _ \        )       )  |() ()|"
	print "          / _  _ \   )        |(_\/_)|  .---.   (        (_ 0 _)"
	print "          |(_)(_)|  ( .---.   (_ /\ _) /     \    .-\"\"-.  |xxx|"
	print "          (_ /\ _)   /     \   |v==v|  |<\ />|   / _  _ \ '---'"
	print "           |wwww|    |(\ /)|(  '-..-'  (_ A _)   |/_)(_\|"
	print "           '-..-'    (_ o _)  )  .---.  |===|    (_ /\ _)"
	print "                      |===|  (  /     \ '---'     |mmmm|"
	print "                      '---'     |{\ /}|           '-..-'"
	print "                                (_ V _)"
	print "                                 |\"\"\"|"
	print "                                 '---'"
	print "                                 "
	print "                                 "
	print "               .  .              .  .   ..                  "
	print "               |__| _.._ ._   .  |__| _.|| _ .    , _  _ ._ "
	print "               |  |(_][_)[_)\_|  |  |(_]||(_) \/\/ (/,(/,[ )"
	print "                      |  |  ._| "

    # We need to reduce the default buffer size to have low latency.
    # It is highly reccomended to use 22050 Hz as samplerate. Works fine also with 44.1K samples
    # but allowes a buffersize of 1 instead of 512 which means approx. 10ms instead of 50 ms latency!
    pygame.mixer.pre_init(22050,-16,1,1)
    pygame.init()
    pygame.joystick.init()
 #   pygame.display.quit()
    # we do not need this event which is thrown permanently by the guitar
    pygame.event.set_blocked(JOYAXISMOTION)

    guitar = pygame.joystick.Joystick(0)
    guitar.init()

    # load config
    config = Config.Config()
    config.loadSongConfig()

    songs = config.getSongs()
    pprint(songs)
    

    # init status
    currentSong = 0
    chordsToPlay = [NO_BUTTON_CHORD]
    playOpen = True
    playing = False
    
    print "Initialization complete"

    while True:
        fist()

# The main loop. Listens to the eventqueue
def fist():
    global guitar, chordsOpen, chordsMuted
    
    # this keeps the application idle until an event is caught
    firstevent= pygame.event.wait()
    # put back the event taken out by wait()
    pygame.event.post(firstevent)
    #print "GotEvent  " + pygame.event.event_name(event.type)
    for event in pygame.event.get():
        if event.type == JOYHATMOTION:
            handleTrigger(event)
        elif event.type == JOYBUTTONDOWN:
            handleButtonDown(event)
        elif event.type == JOYBUTTONUP:
            handleButtonUp(event)


# Handler if the trigger status has changed
# (0,0): Trigger released: stop all chords
# (0,-1): Trigger pushed down: play all chords in the activce chordlist from open chords map
# (0,1): Trigger pulled up: play all chords in the activce chordlist from muted chords map
def handleTrigger(event):
    if event.value == (0,0):
        stopAll()
    elif event.value == (0,-1):
        playOpenChords()
    elif event.value == (0,1):
        playMutedChords()
    elif event.value == (1,0):
        nextSong()

def nextSong():
    global currentSong
    if currentSong == len(songs)-1:
        currentSong = 0
    else:
        currentSong = currentSong + 1
    songs[songs.keys()[currentSong]].getInitSound().play()
    
	

# Handler if a button has been pushed.
# Adds the selected chord to the list of actice chords.
# Removes the cord played when no button is pressed from the list and stops it.
# Immediately plays the chord when the trigger is active
def handleButtonDown(event):
    global chordsToPlay
    chord = getChord(event.button)
    if (chord > 5):
        return

    chordsToPlay.append(chord)

    if (NO_BUTTON_CHORD in chordsToPlay):
        chordsToPlay.remove(NO_BUTTON_CHORD)
        stopChord(NO_BUTTON_CHORD)
    playChord(chord)

# Handler if a button has been released
# Removes the selected chord to the list of actice chords
# Adds the cord played when no button is pressed to the list and plays it if the trigger is active.
# Immediately stops the chord when the trigger is active.
def handleButtonUp(event):
    global chordsToPlay
    chord = getChord(event.button)
    if (chord > 5):
        return

    chordsToPlay.remove(chord)
    if (noButtonPresed()):
        chordsToPlay.append(NO_BUTTON_CHORD)
        playChord(NO_BUTTON_CHORD)
    stopChord(chord)

#stops all chords    
def stopAll():
    global playing
    pygame.mixer.stop()
    playing = False

# stops a single chord    
def stopChord(chord):
    if (chord > 5):
        return

    getCurrentSong().getChord(chord)["down"].stop()
    getCurrentSong().getChord(chord)["up"].stop()

def getCurrentSong():
    global songs, currentSong
    return songs[songs.keys()[currentSong]]

# plays a single chord when the trigger is active 
def playChord(chord):
    global playOpen, playing, chordsMuted, chordsOpen, songs, currentSong

    if (chord > 5):
        return

    # as soon as anyother chord than the NO_BUTTON_CHORD is played stop it, otherwise it may be heard chortly when changing a chord
    if (chord > NO_BUTTON_CHORD):
        stopChord(NO_BUTTON_CHORD)
        
    if (playing and playOpen):
        getCurrentSong().getChord(chord)["down"].play()
    if (playing and not playOpen):
        getCurrentSong().getChord(chord)["up"].play()
    
# plays chords from the active chords list using the open chords samples
def playOpenChords():
    global playing, playOpen, chordsToPlay
    playing = True
    playOpen = True
    for chord in chordsToPlay:
        playChord(chord)


# plays chords from the active chords list using the muted chords samples
def playMutedChords():
    global playing, playOpen, chordsToPlay
    playOpen = False
    playing = True
    for chord in chordsToPlay:
        playChord(chord)
    playing = True



# Helper that equalizes the turner between button 2 and 3

# Rockband USB Guitar
#def getChord(buttonId):
#    if (buttonId == 5):
#	return 42
#    if (buttonId == 0):
#        return 4
#    if (buttonId == 4):
#        return 5
#    return buttonId

# Guitar Hero USB Guitar
def getChord(buttonId):
    if (buttonId == 2):
        return buttonId + 2
    if (buttonId == 3):
        return buttonId
    return buttonId + 1

# Helper that 
def noButtonPresed():
    global guitar
    status =  ( not guitar.get_button(0)\
            and not guitar.get_button(1)\
            and not guitar.get_button(2)\
            and not guitar.get_button(3)\
            and not guitar.get_button(4))
    return status

if __name__ == '__main__':
    main()
