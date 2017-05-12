import  pygame, sys, math

class Groundpoint(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = Rect(pos, size)
        

