import pygame, sys, math, time
from Score import *

class Timer():
    def __init__(self):
        self.startTime = time.clock()

    def update(self):
        newValue = int(time.clock() - self.startTime)
        if newValue != self.value:
            self.value = newValue
            
    def timer(self, time):
       self.update()
       if self.startTime = 0:
           self.startTime = time.clock()
       self.duration = time.clock - self.startTime
       while time > self.duration:
           self.update()
        if self.duration == time:
            self.done == True
            self.startTime = 0
            self.duration = 0
