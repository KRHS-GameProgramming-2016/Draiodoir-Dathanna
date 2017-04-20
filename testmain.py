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
players = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()
fires = pygame.sprite.Group()
plants = pygame.sprite.Group()

Player.containers = all, players
Wall.containers = all, walls
#Enemy.containers = all, enemies
#Fire.containers = all, fires
#Plant.containers = all, plants

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_LEFT:
                player.go("left")
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")

    for enemy in enemies:
        enemy.move()
        
    all.update(size)

    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)
    playerHitsEnemies = pygame.sprite.spritecollide(player, enemies, False)
    playerHitsFires = pygame.sprite.spritecollide(player, walls, False)
    playerHitsPlants = pygame.sprite.spritecollide(player, plants, False)
    enemiesHitWalls = pygame.sprite.groupcollide(enemies, walls, False, False)
    enemiesHitFires = pygame.sprite.groupcollide(enemies, fires, False, False)
    enemiesHitPlants = pygame.sprite.groupcollide(enemies, plants, False, False)

    bgColor = r,g,b
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
