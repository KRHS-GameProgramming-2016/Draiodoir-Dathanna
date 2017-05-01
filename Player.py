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
        self.didBounceY = True
        self.lives = 5
        self.maxSpeed = maxSpeed
        self.activeColor = activeColor
        self.screenHeight = 720
      
    def animate(self):
        if self.prevState != self.state:
            if self.state == "right":
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft

    def update(self, size):
        self.move()
        self.getGravity()

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.animate()
        
    def go(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.didBounceX = False
            self.state = "left"
            self.move()
        if direction == "right":
            self.speedx = self.maxSpeed
            self.didBounceX = False
            self.state = "right"
            self.move()
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.didBounceY = False
            self.state = "up"
            self.move()
            
        if direction == "stop left":
            self.speedx = 0
        if direction == "stop right":
            self.speedx = 0
        if direction == "stop up":
            self.speedy = 0
            
    def getGravity(self):
        if self.didBounceY == False:
            if self.speedy == 0:
                self.speedy = 1
            else:
                self.speedy += .35
            
    def bounceWall(self, other):
        diffX = self.rect.centerx - other.rect.centerx
        diffY = self.rect.centery - other.rect.centery
        if abs(diffX) > abs(diffY): #left right collide
            if diffX > 0: #left
                self.rect.left = other.rect.right + 1
            else:
                self.rect.right = other.rect.left - 1
                self.speedx = 0
        else:
            if diffY > 0: #below
                self.rect.top = other.rect.bottom + 1
            else:
                self.rect.bottom = other.rect.top - 1
                self.didBounceY = True                
                self.speedy = 0

