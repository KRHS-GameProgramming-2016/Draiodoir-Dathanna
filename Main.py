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
players = pygame.sprite.Group()

Wall.containers = all, walls
Player.containers = all, players

level = Level("levels.lvl", 1)
levelNumber = 1
player = Player(level.playerspawn, level.tileSize)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_LEFT:
                player.go("left")
            if event.key == pygame.K_UP:
                player.jump()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
            if event.key == pygame.K_UP:
                player.go("stop up")
    
    
    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)
    
    if player.rect.left > width:
        levelNumber += 1
        level = Level("levels.lvl", levelNumber)
        player = Player(level.playerspawn, level.tileSize)
    
    all.update(size)
    
    for wall in playerHitsWalls:
        player.bounceWall(wall)

    bgColor = r,g,b = 0,0,0
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
