import  pygame, sys, math

class Player():
    
    def __init__(self,  activeColor="red", speed=[0, 0], pos=[0,64]):
        self.imageLeft = pygame.image.load("Resources/Player/Player Left.png")
        self.imageRight = pygame.image.load("Resources/Player/Player Right.png")
        
        self.state = "right"
        self.image = self.imageRight
        self.rect = self.image.get_rect()
        
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.didBounceX = False
        self.didBounceY = False
        self.pos = [self.rect.left, self.rect.top]
        self.lives = 5
        self.maxSpeed = maxSpeed
        self.activeColor = activeColor
      
    def animate(self):
        if self.prevState != self.state:
            if self.state == "right":
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft

    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.animate()
        
    def go(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.state = "left"
            self.move()
        if direction == "right":
            self.speedx = self.maxSpeed
            self.state = "right"
            self.move()
            
        if direction == "stop left":
            self.speedx = 0
        if direction == "stop right":
            self.speedx = 0
