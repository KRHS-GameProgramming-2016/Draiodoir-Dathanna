import  pygame, sys, math
from Wall import *
from Player import *
from Groundpoint import *
from Bridgepoint import *
from Plant import *
from Fire import *
from Enemy import *
from Ladder import *

class Level():
    def __init__(self, levelNumber=1, tileSize=32):
        self.walls = []
        self.enemies = []
        self.fires = []
        self.plants = []
        self.enemies = []
        self.groundpoints = []
        self.bridgepoints = []
        self.ladders = []
        self.tileSize = tileSize
        
        self.loadLevel(levelNumber)

    def unloadLevel(self):
        self.walls = []
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
                if c in "x" :       #enemies
                    self.enemies += [Enemy([x*self.tileSize,
                                        y*self.tileSize], [self.tileSize, self.tileSize])]
                if c in "%" :       #plants
                    self.plants += [Plant([x*self.tileSize,
                                        y*self.tileSize], self.tileSize)]
                if c in "^" :       #fire
                    self.fires += [Fire([x*self.tileSize,
                                        y*self.tileSize], self.tileSize)]
                if c in "." :       #groundpoints
                    self.groundpoints += [Groundpoint([x*self.tileSize,
                                y*self.tileSize], self.tileSize)]
                if c in "#" :       #ladders
                    self.ladders += [Ladder([x*self.tileSize,
                                y*self.tileSize])]
                if c in "~" :       #bridgepoints
                    self.bridgepoints += [Bridgepoint([x*self.tileSize,
                                y*self.tileSize], self.tileSize)]
                                
    def jumpable(self):
        for groundpoint in self.groundpoints:
            for wall in self.walls:
                if groundpoint.rect.centerx == wall.rect.centerx:
                    if abs(groundpoint.rect.bottom - wall.rect.top) < 2:
                        wall.jumpable = True
    def buildBridge(self, bridgepoints):
        for point in bridgepoints:
            Plant(point.rect.topleft)
        
                                        
if __name__ == "__main__":
    level = Level("levels.lvl", 1)
