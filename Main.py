import  pygame, sys, math
from Player import *
from Wall import *
from Groundpoint import *
from Climbpoint import *
from Level import *
from Background import *
from Lives import *
from Fire import *
from Plant import *
from Enemy import *
#from Magic import *
pygame.init()

clock = pygame.time.Clock()

width = 1024
height = 640
size = width, height
screen = pygame.display.set_mode(size)

all = pygame.sprite.OrderedUpdates()
walls = pygame.sprite.Group()
plants = pygame.sprite.Group()
fires = pygame.sprite.Group()
bridgepoints = pygame.sprite.Group()
groundpoints = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
heartdisplays = pygame.sprite.Group()

Wall.containers = all, walls
Plant.containers = all, plants
Fire.containers = all, fires
Groundpoint.containers = all, groundpoints
Bridgepoint.containers = all, bridgepoints
Player.containers = all, players
Enemy.containers = all, enemies
Lives.containers = all, heartdisplays

level = Level(2)
levelNumber = 2

player = Player([1, 416], [64, 96])
heartdisplay = Lives()

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
            if event.key == pygame.K_f:
                if player.activeColor == "green":
                    level.buildBridge(bridgepoints)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
            if event.key == pygame.K_UP:
                player.go("stop up")
    
    
    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)
    playerHitsPlants = pygame.sprite.spritecollide(player, plants, False)
    playerOnGround = pygame.sprite.spritecollide(player, groundpoints, False)
    playerOnFire = pygame.sprite.spritecollide(player, fires, False)
    
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
        
    #if player.rect.top > height:
        #levelNumber += 100
        #px = player.rect.left
        #py = 0
        #pPos = [px, py]
        #for s in all.sprites():
            #s.kill()
        #level = Level(levelNumber)
        #player = Player(pPos, [64, 96], player.speed)
        
    #if player.rect.bottom < 0:
        #levelNumber -= 100
        #px = player.rect.left
        #py = 544
        #pPos = [px, py]
        #for s in all.sprites():
            #s.kill()
        #level = Level(levelNumber)
        #player = Player(pPos, [64, 96], player.speed)
    
    all.update(size)
    
    heartdisplay.change(player.lives)
    
    for wall in playerHitsWalls:
        player.bounceWall(wall)
        
    for plant in playerHitsPlants:
        player.plantcollide(plant)    
        
    for groundpoint in playerOnGround:
        if player.rect.bottom == groundpoint.rect.bottom:
            player.inAir = False
        
    if playerOnFire:
        player.hit = True
        
    if player.hit == True:
        if player.blinkFrame < 12:
            player.blinkImage()
        if player.blinkFrame == 12:
            player.hit = False
            player.blinkFrame = 0
            levelNumber = 1
            pPos = [1, 416]
            for s in all.sprites():
                s.kill()
            player.lives = 5
            level = Level(levelNumber)
            player = Player(pPos, [64, 96], [0, 0])
            heartdisplay = Lives()
        playerLives = player.lives
        
    if len(playerOnGround) == 0:
        player.inAir = True
    
    bgColor = r,g,b = 165,195,235
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
