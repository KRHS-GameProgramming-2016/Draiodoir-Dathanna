import  pygame, sys, math
from Player import *
from Wall import *
from Groundpoint import *
from Level import *
from Background import *
#from Lives import *
#from Fire import *
#from Plant import *
#from Enemy import *
#from Magic import *
pygame.init()

clock = pygame.time.Clock()

width = 1024
height = 640
size = width, height
screen = pygame.display.set_mode(size)

all = pygame.sprite.OrderedUpdates()
walls = pygame.sprite.Group()
groundpoints = pygame.sprite.Group()
players = pygame.sprite.Group()

Wall.containers = all, walls
Groundpoint.containers = all, groundpoints
Player.containers = all, players

level = Level(1)
levelNumber = 1
player = Player([1, 416], [64, 96])
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
    playerOnGround = pygame.sprite.spritecollide(player, groundpoints, False)
    
    if player.rect.left > width:
        levelNumber += 1
        px = 1
        py = player.rect.top
        pPos = [px, py]
        for s in all.sprites():
            s.kill()
        level = Level(levelNumber)
        player = Player(pPos, [64, 96], player.speed)
        
    if player.rect.right < 0:
        levelNumber -= 1
        px = width - 65
        py = player.rect.top
        pPos = [px, py]
        for s in all.sprites():
            s.kill()
        level = Level(levelNumber)
        player = Player(pPos, [64, 96], player.speed)
    
    all.update(size)
    
    for wall in playerHitsWalls:
        player.bounceWall(wall)
        
    for groundpoint in playerOnGround:
        if player.rect.bottom == groundpoint.rect.bottom:
            player.inAir = False
        
    if len(playerOnGround) == 0:
        player.inAir = True

    bgColor = r,g,b = 165,195,235
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
