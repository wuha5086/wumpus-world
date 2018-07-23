import pygame

display_width = 600
display_height = 600
block_width = 150
block_height = 150
x = block_width
y = block_height
crashed = False
black = (0,0,0)
white = (255,255,255)
rect_11 = pygame.Rect((0,0), (x,y))
rect_12 = pygame.Rect((x,0), (x*2,y))
rect_13 = pygame.Rect((x*2,0), (x*3,y))
rect_14 = pygame.Rect((x*3,0), (x*4,y))
rect_21 = pygame.Rect((0,y), (x,y*2))
rect_22 = pygame.Rect((x,y), (x*2,y*2))
rect_23 = pygame.Rect((x*2,y), (x*3,y*2))
rect_24 = pygame.Rect((x*3,y), (x*4,y*2))
rect_31 = pygame.Rect((0,y*2), (x,y*3))
rect_32 = pygame.Rect((x,y*2), (x*2,y*3))
rect_33 = pygame.Rect((x*2,y*2), (x*3,y*3))
rect_34 = pygame.Rect((x*3,y*2), (x*4,y*3))
rect_41 = pygame.Rect((0,y*3), (x,y*4))
rect_42 = pygame.Rect((x,y*3), (x*2,y*4))
rect_43 = pygame.Rect((x*2,y*3), (x*3,y*4))
rect_44 = pygame.Rect((x*3,y*3), (x*4,y*4))

x_0 = 0
x_1 = x
x_2 = x*2
x_3 = x*3

y_0 = 0
y_1 = y
y_2 = y*2
y_3 = y*3

goldFlag = 0
startFlag = 0
timeDelay = 1000
lastDirection = "right"
right = "right"
left = "left"
down = "down"
up = "up"
tempDirection = ""




