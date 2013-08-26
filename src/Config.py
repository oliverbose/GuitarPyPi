#!/usr/bin/python
import pygame
import xml.etree.ElementTree as ET


class Song:

    def getInitSound(self):
        return self.initSound

    def setInitSound(self,initSound):
        self.initSound = initSound

    def getChord(self, chord):
        return self.chords[chord]

    def setChords(self,chords):
        self.chords = chords
        
    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

    def getName(name):
        return self.name

    def setName(self,name):
        self.name = name

class Config:

    def __init__(self):
        self.songs = {}

    def loadSongConfig(self):
        tree = ET.parse('../songs/test1.song')
        chords = {}
        song = Song()
        root = tree.getroot()
        song.setId(root.attrib["id"])
        song.setName(root.attrib["name"])
        song.setInitSound(pygame.mixer.Sound(root.attrib["initSound"]))
        for chordEl in root.iter('chord'):
            sounds = {}
            for soundEl in chordEl.iter('sound'):
                sounds[soundEl.attrib["id"]] =  pygame.mixer.Sound(soundEl.attrib["file"])

            chords[int(chordEl.attrib["id"])] = sounds 
        song.setChords(chords)
        self.songs[song.getId()] = song
        

    def getSongs(self):
        return self.songs
    
    
