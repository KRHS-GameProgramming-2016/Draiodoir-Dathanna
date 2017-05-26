import  pygame, sys, math

class Fire():
    def __init__(self, image, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/Wall/" + image + ".png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(topleft = pos)
