import  pygame, sys, math

class Lives(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.oneLifeImage = pygame.image.load("rsc/Lives/hearts1life.png")
        self.twoLivesImage = pygame.image.load("rsc/Lives/hearts2lives.png")
        self.threeLivesImage = pygame.image.load("rsc/Lives/hearts3lives.png")
        self.fourLivesImage = pygame.image.load("rsc/Lives/hearts4lives.png")
        self.fiveLivesImage = pygame.image.load("rsc/Lives/hearts5lives.png")
        
        self.image = self.fiveLivesImage
        self.rect = self.image.get_rect(topleft = pos)
        self.value = 5

    def change(self, playerLives):
        newValue = playerLives
        if newValue != self.value:
            self.value = newValue
            if self.value == 5:
                self.image = self.fiveLivesImage
            if self.value == 4:
                self.image = self.fourLivesImage
            if self.value == 3:
                self.image = self.threeLivesImage
            if self.value == 2:
                self.image = self.twoLivesImage
            if self.value == 1:
                self.image = self.oneLifeImage
            self.rect = self.image.get_rect(center = self.rect.center)
