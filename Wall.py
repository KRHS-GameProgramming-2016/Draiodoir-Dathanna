import  pygame, sys, math

class Wall():
    def __init__(self, image, pos):
        self.image = pygame.image.load("Resources/Wall/" + image + ".png")
        self.rect = self.image.get_rect(center = pos)
        
