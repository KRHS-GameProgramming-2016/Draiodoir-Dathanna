import  pygame, sys, math
from Wall import *
from Player import *
from Groundpoint import *

class Level():
    def __init__(self, levelFile, levelNumber=1, tileSize=32):
        self.walls = []
        self.players = []
        self.enemies = []
        self.fires = []
        self.plants = []
        self.playerSpawns = []
        self.tileSize = tileSize

        self.loadLevel(levelFile, levelNumber)
        self.loadGroundpoints(levelFile, levelNumber)

    def unloadLevel(self):
        self.walls = []
        self.player = []
        self.enemySpawn = []

    def loadLevel(self, levelFile, levelNumber):
        f = open("rsc/Levels/levels.lvl")
        lines = f.readlines()
        f.close()

        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]

        lines = newlines

        startIndex = lines.index(str(levelNumber))+1
        endIndex = startIndex + 20

        newlines = []
        for line in range(startIndex, endIndex):
            #print lines[line]
            newlines += [lines[line]]
        lines = newlines

        for line in lines:
            print line

        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c in "w" :       #walls
                    Wall("purplebricks", [x*self.tileSize,
                                        y*self.tileSize], self.tileSize)
                if c in "*" :
                    self.playerspawn = [x*self.tileSize,
                                        y*self.tileSize]
                                        
    def loadGroundpoints(self, levelFile, levelNumber):
        f = open("rsc/Levels/groundpoints.lvl")
        lines = f.readlines()
        f.close()

        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]

        lines = newlines

        startIndex = lines.index(str(levelNumber))+1
        endIndex = startIndex + 20

        newlines = []
        for line in range(startIndex, endIndex):
            #print lines[line]
            newlines += [lines[line]]
        lines = newlines

        for line in lines:
            print line

        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c in "." :       #walls
                    Groundpoint([x*self.tileSize,
                                y*self.tileSize], self.tileSize)
                                
                                               
if __name__ == "__main__":
    level = Level("levels.lvl", 1)
