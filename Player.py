import  pygame, sys, math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos=[0,64], size=None, activeColor="red", speed=[0, 0], maxSpeed=5):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.imageLeft = pygame.image.load("rsc/Player/Player Left.png")
        self.imageRight = pygame.image.load("rsc/Player/Player Right.png")
        
        self.prevState = "right"
        self.state = "right"
        if size:
            self.imageRight = pygame.transform.scale(self.imageRight, [size,size])            
            self.imageLeft = pygame.transform.scale(self.imageLeft, [size,size])            
        self.image = self.imageRight
        self.rect = self.image.get_rect(center = pos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.didBounceX = False
        self.didBounceY = False
        self.lives = 5
        self.maxSpeed = maxSpeed
        self.activeColor = activeColor
      
    def animate(self):
        if self.prevState != self.state:
            if self.state == "right":
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft

    def update(self, size):
        self.move()

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
            
    def bounceWall(self, other):
        if not self.didBounceX: 
            self.speedx = -self.speedx
            self.didBounceX = True
            self.speedx = 0
        if not self.didBounceY:
            self.speedy = -self.speedy
            self.didBounceY = True
            self.speedy = 0
