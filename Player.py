import  pygame, sys, math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos=[0,64], size=None, speed=[0, 0], activeColor="green", maxSpeed=5):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.imageLeft = pygame.image.load("rsc/Player/Player Left.png")
        self.imageRight = pygame.image.load("rsc/Player/Player Right.png")
        self.blankImage = pygame.image.load("rsc/Player/blank.png")
        
        self.prevState = "right"
        self.state = "right"
        self.inAir = False
        if size:
            self.imageRight = pygame.transform.scale(self.imageRight, size)            
            self.imageLeft = pygame.transform.scale(self.imageLeft, size)            
        self.image = self.imageRight
        self.rect = self.image.get_rect(topleft = pos)

        self.speedx = speed[0]
        self.speedy = speed[1]
        self.didBounceX = False
        self.didBounceY = False
        self.lives = 5
        self.maxSpeed = maxSpeed
        self.maxSpeedy = 8
        self.activeColor = activeColor
        self.screenHeight = 720
        self.blinkFrame = 0
        self.hit = False
        
        self.climb = False
      
    def animate(self):
        if self.prevState != self.state:
            if self.state == "right":
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft

    def blinkImage(self):
        if self.blinkFrame == 0:
            self.lives -= 1
            self.prevImage = self.image
            self.blinkFrame = 1
            
        self.blinkFrame1 = self.prevImage
        self.blinkFrame2 = self.blankImage
        
        if self.blinkFrame > 0:
            if self.blinkFrame % 4 == 0:
                self.image = self.blinkFrame2
            if self.blinkFrame % 4 != 0:
                self.image = self.blinkFrame1
            self.blinkFrame += 1

    def update(self, size):
        self.move()

    def move(self):
        if not self.climb:
            self.getGravity()
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.animate()
        
        
    def go(self, direction):
        if direction == "left":
            self.didBounceY = False            
            self.speedx = -self.maxSpeed
            self.didBounceX = False
            self.state = "left"
            self.move()
            self.didBounceY = False
            self.climb = False
        if direction == "right":
            self.didBounceY = False
            self.speedx = self.maxSpeed
            self.didBounceX = False
            self.didBounceY = False
            self.state = "right"
            self.move()
            self.didBounceY = False
            self.climb = False
        if direction == "up":
            self.didBounceY = False
            self.speedy = -self.maxSpeed
            self.didBounceX = False
            self.didBounceY = False
            self.state = "up"
            self.move()
            self.didBounceY = False
        if direction == "down":
            self.didBounceY = False
            self.speedy = self.maxSpeed
            self.didBounceX = False
            self.didBounceY = False
            self.state = "down"
            self.move()
            self.didBounceY = False
            
        if direction == "stop left":
            self.speedx = 0
            self.didBounceY = False
            self.getGravity()
        if direction == "stop right":
            self.speedx = 0
            self.didBounceY = False
            self.getGravity()
        if direction == "stop up":
            self.speedy = 0
            self.didBounceY = False
        if direction == "stop down":
            self.speedy = 0
            self.didBounceY = False
            
    def up(self):
        if self.climb == True:
            self.go("up")
        else:
            self.jump()
            
    def power(self, color):
        if self.color == "green":
            self.plantbuild()
            
    def jump(self, auto=None):
        if not self.inAir:
            self.speedy = -self.maxSpeedy
            if auto == "auto":
                if self.speedx < 0:
                    self.speedx = -4
                if self.speedx > 0:
                    self.speedx = 4
            self.didBounceY = False
            self.move()
            self.inAir = True
        
    def getGravity(self):
        if self.inAir == True:
            if self.speedy == 0:
                self.speedy = 1
            else:
                self.speedy += .42
            
    def bounceWall(self, other):
        diffX = self.rect.centerx - other.rect.centerx
        diffY = self.rect.centery - other.rect.centery
        if abs(diffX) > abs(diffY): #left right collide
            if diffX > 0: #left
                if diffY < 15:
                    if other.jumpable == True:
                        if self.speedy == 0:
                            self.jump("auto")
                else:
                    self.rect.left = other.rect.right + 1
            else:
                if diffY < 30:
                    if other.jumpable == True:
                        if self.speedy == 0:
                            self.jump("auto")
                else:
                    self.rect.right = other.rect.left - 1
                #self.speedx = 0
        else:
            if diffY > 0: #below
                self.rect.top = other.rect.bottom + 1
            else:
                self.rect.bottom = other.rect.top - 1               
            self.speedy = 0
            self.didBounceY = True
            self.inAir = False
            
    def plantcollide(self, other):
        diffX = self.rect.centerx - other.rect.centerx
        diffY = self.rect.centery - other.rect.centery
        if abs(diffX) > abs(diffY): #left right collide
            if diffX > 0: #left
                self.rect.left = other.rect.right + 1
                self.speedx = 0
            else:
                self.rect.right = other.rect.left - 1
                self.speedx = 0
        else:
            if diffY > 0: #below
                self.rect.top = other.rect.bottom + 1
            else:
                self.rect.bottom = other.rect.top - 1               
            self.speedy = 0
            self.didBounceY = True
            self.inAir = False
            
        

