import pygame
import random
import c

class Block:
	def __init__(self):
		self.breeze = False
		self.player = False
		self.wumpus = False
		self.pit = False
		self.scream = False
		self.gold = False
		self.glitter = False
		self.blank = True

grid = [[Block() for j in range(4)] for i in range(4)]

pgrid = [[Block() for j in range(4)] for i in range(4)]

visited = [[0 for j in range(4)] for i in range(4)]

class Player:
	def __init__(self):
		self.arrow = True
		self.gold = False
"""	
def createPlayer(player):
	global player_x, player_y, a_x, a_y
	seed_x = 0
	seed_y = 3
	a_x = seed_x
	a_y = seed_y
	player_x = c.x*seed_x
	player_y = c.y*seed_y
	grid[0][3].player = True
	grid[0][3].blank = False
	gameDisplay.blit(player, (player_x,player_y))
	
def createGold(gold):

	global gold_x, gold_y, g_x, g_y
	gold_x = 0
	gold_y = 3

	

	while True:
		seed_x = random.randint(0,3)
		seed_y = random.randint(0,3)
		g_x = seed_x
		g_y = seed_y
		gold_x = c.x*seed_x
		gold_y = c.y*seed_y
		print(seed_x)
		print(seed_y)
		if grid[seed_x][seed_y].blank:
			grid[seed_x][seed_y].gold = True
			grid[seed_x][seed_y].blank = False
			if seed_x!=0: 
				grid[seed_x-1][seed_y].glitter = True
				grid[seed_x-1][seed_y].blank = False
			if seed_x!=3:
				grid[seed_x+1][seed_y].glitter = True
				grid[seed_x+1][seed_y].blank = False
			if seed_y!=0:
				grid[seed_x][seed_y-1].glitter = True
				grid[seed_x][seed_y-1].blank = False
			if seed_y!=3:
				grid[seed_x][seed_y+1].glitter = True
				grid[seed_x][seed_y+1].blank = False
				
			break
	gameDisplay.blit(gold, (gold_x,gold_y))
	

def createWumpus(wumpus):

	global w_x, w_y, wu_x, wu_y
	w_x = 0
	w_y = c.y*3

	while True:
		seed_x = random.randint(0,3)
		seed_y = random.randint(0,3)
		wu_x = seed_x
		wu_y = seed_y
		w_x = c.x*seed_x
		w_y = c.y*seed_y
		print(seed_x)
		print(seed_y)
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
	gameDisplay.blit(wumpus, (w_x,w_y))
	

def createPit(pit):

	global pit_x, pit_y, p_x, p_y
	pit_x = 0
	pit_y = c.y*3
	while True:
		seed_x = random.randint(0,3)
		seed_y = random.randint(0,3)
		p_x = seed_x
		p_y = seed_y
		pit_x = c.x*seed_x
		pit_y = c.y*seed_y
	
		if grid[seed_x][seed_y].blank:
			if seed_x == 0 and seed_y == 2 and (grid[1][3].blank!= True or grid[1][3].gold!= True) :
				continue
			if seed_x == 1 and seed_y == 3 and (grid[0][2].blank!= True or grid[0][2].gold!= True) :
				continue	
			grid[seed_x][seed_y].pit = True
			grid[seed_x][seed_y].blank = False
			if seed_x!=0: 
				grid[seed_x-1][seed_y].breeze = True
				grid[seed_x-1][seed_y].blank = False
			if seed_x!=3:
				grid[seed_x+1][seed_y].breeze = True
				grid[seed_x+1][seed_y].blank = False
			if seed_y!=0:
				grid[seed_x][seed_y-1].breeze = True
				grid[seed_x][seed_y-1].blank = False
			if seed_y!=3:
				grid[seed_x][seed_y+1].breeze = True
				grid[seed_x][seed_y+1].blank = False
				
			break
	gameDisplay.blit(pit, (pit_x,pit_y))

def drawGrid(x,y):
	pygame.draw.line(gameDisplay, c.black, (x,0),(x,y*4))
	pygame.draw.line(gameDisplay, c.black, (x*2,0),(x*2,y*4))
	pygame.draw.line(gameDisplay, c.black, (x*3,0),(x*3,y*4))
	pygame.draw.line(gameDisplay, c.black, (0,y),(x*4,y))
	pygame.draw.line(gameDisplay, c.black, (0,y*2),(x*4,y*2))
	pygame.draw.line(gameDisplay, c.black, (0,y*3),(x*4,y*3))

def createWorld(player, wumpus, pit, gold):
	global grid, gameDisplay, clock, emptyBox
	gameDisplay = pygame.display.set_mode((c.display_width, c.display_height))
	pygame.display.set_caption('Wumpus World AI by sushrut')
	clock = pygame.time.Clock()
	gameDisplay.fill(c.white)
	emptyBox = pygame.Surface((c.x,c.y))
	emptyBox.fill(c.white)
	drawGrid(c.x,c.y)
	createPlayer(player)
	createGold(gold)
	createWumpus(wumpus)
	createPit(pit)
	createPit(pit)

"""


