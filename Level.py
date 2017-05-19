import  pygame, sys, math
from Wall import *
from Player import *
from Groundpoint import *

class Level():
    def __init__(self, levelNumber=1, tileSize=32):
        self.walls = []
        self.players = []
        self.enemies = []
        self.fires = []
        self.plants = []
        self.groundpoints = []
        self.tileSize = tileSize
        
        self.loadLevel(levelNumber)

    def unloadLevel(self):
        self.walls = []
        self.playerSpawns = []
        self.groundpoints = []

    def loadLevel(self, levelNumber):
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
                    self.walls += [Wall("purplebricks", [x*self.tileSize,
                                        y*self.tileSize], self.tileSize)]
                if c in "." :       #groundpoints
                    self.groundpoints += [Groundpoint([x*self.tileSize,
                                y*self.tileSize], self.tileSize)]
                                        
if __name__ == "__main__":
    level = Level("levels.lvl", 1)
