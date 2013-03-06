GuitarPyPi
==========

Play real music on your Guitar Hero(R)-controller connected to a RaspberryPi (that's the "Pi")!
The goal is to use the controller to play a predefined set of chords.

This is done in Python (that's the "Py") heavily relying on the pygames library.

The guitar-sounds are stored as OGG files. By default there are 13 powercords (E to E8 in halftones) recorded 
with a distorted 1988 Fender Stratocaster. Every chord is sampled as open and muted. 
Feel free to use your own samples in WAV or OGG format.

How to play
-----------
There five colored buttons on the neck of the guitar are used to select the chord you want to play. 
Assuming no button pressed is also a state there are six chords.

The selected chord is played when the trigger is pulled up or pushed down.

To fulfill the need of different strumming styles (open and muted) the open chords are played when the trigger is pushed down
and the muted when pulled up.

The "back" and "start" buttons will be used to select different songs, a sample is played back wen the song is switched to
hav feed back when there is no display (not yet implemented).


Configuration (not yet implemented)
-----------------------------------
The configuration is done in an XML-file. There is a set of main properties for the app and a set of songsconfigurations
which consist the mapping of the buttons to samples.
The application config has following attributes:
- JoystickId: The joystick-id of your guitar. In most cases it is 0 for /dev/input/js0
For the following refer to http://www.pygame.org/docs/ref/mixer.html for detailed information.
- SampleRate: The sample rate youre samples are recorded with. (defaults to 44100)
- BitDepth: The bit depth youre samples are recorded with (defaults to -16)
- Channels: The number of channels in your samples (1 = mono, 2 = stereo)
- BufferSize: Number of samples sent to the OS at once. Lower number gives lower latency (the time between you trigger and hear the sound) but can lead to dropouts.
- ReadySound: a Sample that is played when the system is ready (usefull if you have no display)


Installation
------------
- Checkout the repository from github.com to ~/GuitarPyPi
- make sure you have the guitar connected and your OS recognizes it as a joystick.
	- ls /dev/input should list you 'js0'
	- dmesg |grep Guitar should show two lines, one listed as "input"
	- jstest /dev/input/js0 should show you the changes of button states.
- go to ~/GuitarPyPi/src
- make sure the GuitarPyPi.py is executable
- run ./GuitarPyPi.py

Requirements
------------
For the RedOctane USB-controller youn need
- a RaspberryPi Model B (Model A untested)
- An SD-card with Raspbian (Kernel 3.6.11+) and installed xpad kernel module


Roadmap
-------
Following things have to be done:
	- Configuration via XML
	- Enhanced chord change (while the trigger is active) 
	- Support of bluetooth controllers
	- create a "headless" raspian installation, that automatically starts GuitarPyPi after boot.
	- use display connected to GPIO (some day...)
