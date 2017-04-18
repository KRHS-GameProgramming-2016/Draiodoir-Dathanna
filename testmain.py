import  pygame, sys, math
from Player import *
from Wall import *
from Level import *
from Background import *
#from Lives import *
#from Fire import *
#from Plant import *
#from Enemy import *
#from Magic import *
pygame.init()

clock = pygame.time.Clock()

width = 960
height = 720
size = width, height
screen = pygame.display.set_mode(size)

all = pygame.sprite.OrderedUpdates()
walls = pygame.sprite.Group()
Wall.containers = all, walls

#player = Player()

level = Level("levels.lvl", 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    all.update(size)

    bgColor = r,g,b = 0,0,0
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
