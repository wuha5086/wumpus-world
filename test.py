import pygame
import random
from c import *
from w import *
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Wumpus World AI by sushrut')
clock = pygame.time.Clock()

#define empty space
emptyBox = pygame.Surface((x,y))

#Import and scale images
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (x,y))

wumpusImg = pygame.image.load('wumpus.png')
wumpusImg = pygame.transform.scale(wumpusImg, (x,y))

pitImg = pygame.image.load('pit.jpeg')
pitImg = pygame.transform.scale(pitImg, (x,y))

goldImg = pygame.image.load('gold.jpeg')
goldImg = pygame.transform.scale(goldImg, (x,y))

#define 4x4 matrix of the world
grid = [[Block() for j in range(4)] for i in range(4)]

#=====CREATE WORLD=====#
start = grid[0][3]
player_x = 0
player_y = 0

def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def drawGrid(x,y):
    pygame.draw.line(gameDisplay, black, (x,0),(x,y*4))
    pygame.draw.line(gameDisplay, black, (x*2,0),(x*2,y*4))
    pygame.draw.line(gameDisplay, black, (x*3,0),(x*3,y*4))
    pygame.draw.line(gameDisplay, black, (0,y),(x*4,y))
    pygame.draw.line(gameDisplay, black, (0,y*2),(x*4,y*2))
    pygame.draw.line(gameDisplay, black, (0,y*3),(x*4,y*3))


gameDisplay.fill(white)
emptyBox.fill(white)
drawGrid(x,y)

#Create Agent
seed_x = 0
seed_y = 3
a_x = seed_x
a_y = seed_y
player_x = x*seed_x
player_y = y*seed_y
grid[0][3].player = True
grid[0][3].blank = False
gameDisplay.blit(playerImg, (player_x,player_y))
agent = Player()

#Create Gold
gold_x = 0
gold_y = 3
while True:
    seed_x = random.randint(0,3)
    seed_y = random.randint(0,3)
    g_x = seed_x
    g_y = seed_y
    gold_x = x*seed_x
    gold_y = y*seed_y
    
    if grid[seed_x][seed_y].blank:
        grid[seed_x][seed_y].gold = True
        grid[seed_x][seed_y].blank = False
        if seed_x!=0: 
            grid[seed_x-1][seed_y].glitter = True
            
        if seed_x!=3:
            grid[seed_x+1][seed_y].glitter = True
            
        if seed_y!=0:
            grid[seed_x][seed_y-1].glitter = True
            
        if seed_y!=3:
            grid[seed_x][seed_y+1].glitter = True
            
            
        break
gameDisplay.blit(goldImg, (gold_x,gold_y))
    
#Create wumpus
w_x = 0
w_y = y*3

while True:
    seed_x = random.randint(0,3)
    seed_y = random.randint(0,3)
    wu_x = seed_x
    wu_y = seed_y
    w_x = x*seed_x
    w_y = y*seed_y
    
    if(seed_x != 0 and seed_y != 3):
        grid[seed_x][seed_y].wumpus = True
        grid[seed_x][seed_y].blank = False
        if seed_x!=0: 
            grid[seed_x-1][seed_y].scream = True
        if seed_x!=3:
            grid[seed_x+1][seed_y].scream = True
        if seed_y!=0:
            grid[seed_x][seed_y-1].scream = True
        if seed_y!=3:
            grid[seed_x][seed_y+1].scream = True
        break
gameDisplay.blit(wumpusImg, (w_x,w_y))
    
#Create pit 1
pit_x1 = 0
pit_y1 = y*3
while True:
    seed_x = random.randint(0,3)
    seed_y = random.randint(0,3)
    p_x1 = seed_x
    p_y1 = seed_y
    pit_x1 = x*seed_x
    pit_y1 = y*seed_y

    if grid[seed_x][seed_y].blank:
        if seed_x == 0 and seed_y == 2 and (grid[1][3].blank!= True or grid[1][3].gold!= True) :
            continue
        if seed_x == 1 and seed_y == 3 and (grid[0][2].blank!= True or grid[0][2].gold!= True) :
            continue    
        grid[seed_x][seed_y].pit = True
        grid[seed_x][seed_y].blank = False
        if seed_x!=0: 
            grid[seed_x-1][seed_y].breeze = True
            
        if seed_x!=3:
            grid[seed_x+1][seed_y].breeze = True
            
        if seed_y!=0:
            grid[seed_x][seed_y-1].breeze = True
            
        if seed_y!=3:
            grid[seed_x][seed_y+1].breeze = True
            
            
        break
gameDisplay.blit(pitImg, (pit_x1,pit_y1))

#Create pit 2
pit_x2 = 0
pit_y2 = y*3
while True:
    seed_x = random.randint(0,3)
    seed_y = random.randint(0,3)
    p_x2 = seed_x
    p_y2 = seed_y
    pit_x2 = x*seed_x
    pit_y2 = y*seed_y

    if grid[seed_x][seed_y].blank:
        if seed_x == 0 and seed_y == 2 and (grid[1][3].blank!= True or grid[1][3].gold!= True) :
            continue
        if seed_x == 1 and seed_y == 3 and (grid[0][2].blank!= True or grid[0][2].gold!= True) :
            continue    
        grid[seed_x][seed_y].pit = True
        grid[seed_x][seed_y].blank = False
        if seed_x!=0: 
            grid[seed_x-1][seed_y].breeze = True
            
        if seed_x!=3:
            grid[seed_x+1][seed_y].breeze = True
            
        if seed_y!=0:
            grid[seed_x][seed_y-1].breeze = True
            
        if seed_y!=3:
            grid[seed_x][seed_y+1].breeze = True
            
            
        break
gameDisplay.blit(pitImg, (pit_x2,pit_y2))

#=====DEFINE ACTIONS====#

x_ch = 0
y_ch = 0

def moveRight():
    global x_ch, y_ch, player_y, player_x, a_x, a_y
    if player_x != x*3:
        x_ch = x
        player(player_x+x_ch,player_y+y_ch)
        gameDisplay.blit(emptyBox, (player_x,player_y))
        player_x = player_x+x_ch
        player_y = player_y+y_ch
        x_ch = 0
        y_ch = 0
        a_x = a_x+1

def moveLeft():
    global x_ch, y_ch, player_y, player_x, a_x, a_y
    if player_x != 0:
        x_ch = -x
        player(player_x+x_ch,player_y+y_ch)
        gameDisplay.blit(emptyBox, (player_x,player_y))
        player_x = player_x+x_ch
        player_y = player_y+y_ch
        x_ch = 0
        y_ch = 0
        a_x = a_x-1

def moveUp():
    global x_ch, y_ch, player_y, player_x, a_x, a_y
    if player_y != 0:
        y_ch = -y
        player(player_x+x_ch,player_y+y_ch)
        gameDisplay.blit(emptyBox, (player_x,player_y))
        player_x = player_x+x_ch
        player_y = player_y+y_ch
        x_ch = 0
        y_ch = 0
        a_y = a_y -1

def moveDown():
    global x_ch, y_ch, player_y, player_x, a_x, a_y
    if player_y != y*3:
        y_ch = y
        player(player_x+x_ch,player_y+y_ch)
        gameDisplay.blit(emptyBox, (player_x,player_y))
        player_x = player_x+x_ch
        player_y = player_y+y_ch
        x_ch = 0
        y_ch = 0
        a_y = a_y+1

def shoot(direction):
    if agent.arrow == False:
        print("Out of arrows!")
        return
    agent.arrow = False
    if direction == "right" and a_x !=3 :
        if grid[a_x+1][a_y].wumpus:
            grid[a_x+1][a_y].wumpus = False
            print("Wumpus Killed!")
            gameDisplay.blit(emptyBox, (x*(a_x+1),y*a_y))
            grid[a_x][a_y].scream = False
            if a_x+1 != 3:
                grid[a_x+2][a_y].scream = False
                if grid[a_x+2][a_y].pit:
                    grid[a_x+1][a_y].breeze = True
                if grid[a_x+2][a_y].gold:
                    grid[a_x+1][a_y].glitter = True
            if a_y != 0:
                grid[a_x+1][a_y-1].scream = False
                if grid[a_x+1][a_y-1].pit:
                    grid[a_x+1][a_y].breeze = True
                if grid[a_x+1][a_y-1].gold:
                    grid[a_x+1][a_y].glitter = True
            if a_y != 3:
                grid[a_x+1][a_y+1].scream = False
                if grid[a_x+1][a_y+1].pit:
                    grid[a_x+1][a_y].breeze = True
                if grid[a_x+1][a_y+1].gold:
                    grid[a_x+1][a_y].glitter = True

    if direction == "left" and a_x !=0 :
        if grid[a_x-1][a_y].wumpus:
            grid[a_x-1][a_y].wumpus = False
            print("Wumpus Killed!")
            gameDisplay.blit(emptyBox, (x*(a_x-1),y*a_y))
            grid[a_x][a_y].scream = False
            if a_x-1 != 0:
                grid[a_x-2][a_y].scream = False
                if grid[a_x-2][a_y].pit:
                    grid[a_x-1][a_y].breeze = True
                if grid[a_x-2][a_y].gold:
                    grid[a_x-1][a_y].glitter = True
            if a_y != 0:
                grid[a_x-1][a_y-1].scream = False
                if grid[a_x-1][a_y-1].pit:
                    grid[a_x-1][a_y].breeze = True
                if grid[a_x-1][a_y-1].gold:
                    grid[a_x-1][a_y].glitter = True
            if a_y != 3:
                grid[a_x-1][a_y+1].scream = False
                if grid[a_x-1][a_y+1].pit:
                    grid[a_x-1][a_y].breeze = True
                if grid[a_x-1][a_y+1].gold:
                    grid[a_x-1][a_y].glitter = True

    if direction == "up" and a_y !=0 :
        if grid[a_x][a_y-1].wumpus:
            grid[a_x][a_y-1].wumpus = False
            print("Wumpus Killed!")
            print(a_x)
            print(a_y)
            gameDisplay.blit(emptyBox, (x*a_x,y*(a_y-1)))
            grid[a_x][a_y].scream = False
            if a_y-1 != 0:
                grid[a_x][a_y-2].scream = False
                if grid[a_x][a_y-2].pit:
                    grid[a_x][a_y-1].breeze = True
                if grid[a_x][a_y-2].gold:
                    grid[a_x][a_y-1].glitter = True
            if a_x != 0:
                grid[a_x-1][a_y-1].scream = False
                if grid[a_x-1][a_y-1].pit:
                    grid[a_x][a_y-1].breeze = True
                if grid[a_x-1][a_y-1].gold:
                    grid[a_x][a_y-1].glitter = True
            if a_x != 3:
                grid[a_x+1][a_y-1].scream = False
                if grid[a_x+1][a_y-1].pit:
                    grid[a_x][a_y-1].breeze = True
                if grid[a_x+1][a_y-1].gold:
                    grid[a_x][a_y-1].glitter = True

    if direction == "down" and a_y !=3 :
        if grid[a_x][a_y+1].wumpus:
            grid[a_x][a_y+1].wumpus = False
            print("Wumpus Killed!")
            gameDisplay.blit(emptyBox, (x*a_x,y*(a_y+1)))
            grid[a_x][a_y].scream = False
            if a_y+1 != 3:
                grid[a_x][a_y+2].scream = False
                if grid[a_x][a_y+2].pit:
                    grid[a_x][a_y+1].breeze = True
                if grid[a_x][a_y+2].gold:
                    grid[a_x][a_y+1].glitter = True
            if a_x != 0:
                grid[a_x-1][a_y+1].scream = False
                if grid[a_x-1][a_y-1].pit:
                    grid[a_x][a_y+1].breeze = True
                if grid[a_x-1][a_y-1].gold:
                    grid[a_x][a_y+1].glitter = True
            if a_x != 3:
                grid[a_x+1][a_y+1].scream = False
                if grid[a_x+1][a_y+1].pit:
                    grid[a_x][a_y+1].breeze = True
                if grid[a_x+1][a_y+1].gold:
                    grid[a_x][a_y+1].glitter = True


#====GAMEPLAY EVENT HANDLING====#

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight()
            if event.key == pygame.K_LEFT:
                moveLeft()
            if event.key == pygame.K_UP:
                moveUp()
            if event.key == pygame.K_DOWN:
                moveDown()
            if event.key == pygame.K_w:
                shoot("up")
            if event.key == pygame.K_s:
                shoot("down")
            if event.key == pygame.K_a:
                shoot("left")
            if event.key == pygame.K_d:
                shoot("right")
    if grid[a_x][a_y].gold == True and goldFlag!=1:
        goldFlag = 1
        agent.gold = True
        print("Gold Collected!")
    if grid[a_x][a_y] == start and agent.gold == True:
        print("You Won!")
        break
    if grid[a_x][a_y].wumpus == True or grid[a_x][a_y].pit == True :
        print ("Game Over!")
        break
    drawGrid(x,y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()


#=====AGENT AI=====#

