#!/usr/bin/python
import pygame
import xml.etree.ElementTree as ET
from os import listdir


class Song:

    def __init__(self,tree):
        chords = {}
        root = tree.getroot()
        self.setId(root.attrib["id"])
        self.setName(root.attrib["name"])
        self.setInitSound(pygame.mixer.Sound(root.attrib["initSound"]))
        for chordEl in root.iter('chord'):
            sounds = {}
            for soundEl in chordEl.iter('sound'):
                sounds[soundEl.attrib["id"]] = pygame.mixer.Sound(soundEl.attrib["file"])
            
            chords[int(chordEl.attrib["id"])] = sounds
        
        self.setChords(chords)

    def getInitSound(self):
        return self.initSound

    def setInitSound(self,initSound):
        self.initSound = initSound

    def getChord(self, chord):
        return self.chords[chord]

    def setChords(self,chords):
        self.chords = chords
        
    def getId(self):
        return self.anId

    def setId(self,anId):
        self.anId = anId

    def getName(self,name):
        return self.name

    def setName(self,name):
        self.name = name

class Config:

    def __init__(self):
        self.songs = {}

    def loadSongConfig(self):
        filelist = listdir("../songs");
        for songfile in filelist:
            if songfile.endswith("song"):
                tree = ET.parse("../songs/" + songfile)
                song = Song(tree)
                self.songs[song.getId()] = song
        
    def getSongs(self):
        return self.songs
    
    
