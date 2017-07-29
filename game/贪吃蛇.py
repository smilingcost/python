import pygame, sys, random  
from pygame.locals import *  
  
pygame.init()  
mainClock = pygame.time.Clock()  
  
WINDOWWIDTH = 400  
WINDOWHEIGHT = 400  
rectLength = 18  
  
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)  
pygame.display.set_caption('Snake')  
  
BLACK = (0,0,0)  
GREEN = (0,255,0)  
  
snakeRect = []  
for i in range(7,10):  
    snakeRect.append(pygame.Rect(i*(rectLength+2)+1,0+1,rectLength,rectLength))  
food = pygame.Rect(5*(rectLength+2),5*(rectLength+2),rectLength+2,rectLength+2)     
moveLeft = True  
moveRight = False  
moveUp = False  
moveDown = False  
  
direction = 1  
foodImage = pygame.image.load("C:\Users\Administrator\Desktop\cherry.png")
while True:
    for event in pygame.event.get():  
        if event.type == QUIT:  
            pygame.quit()  
            sys.exit()  
        if event.type == KEYDOWN:  
            if event.key == K_LEFT and moveRight==False:  
                moveLeft = True  
                moveRight = False  
                moveUp = False  
                moveDown = False  
            if event.key == K_RIGHT and moveLeft==False:  
                moveLeft = False  
                moveRight = True  
                moveUp = False  
                moveDown = False  
            if event.key == K_UP and moveDown==False:  
                moveLeft = False  
                moveRight = False  
                moveUp = True  
                moveDown = False  
            if event.key == K_DOWN and moveUp==False:  
                moveLeft = False  
                moveRight = False  
                moveUp = False  
                moveDown = True  
    head = pygame.Rect(snakeRect[0].left,snakeRect[0].top,snakeRect[0].width,snakeRect[0].height)  
    if moveLeft == True:  
        head.right = head.left-2  
    if moveRight == True:  
        head.left = head.right+2  
    if moveUp == True:  
        head.bottom = head.top-2  
    if moveDown == True:  
        head.top = head.bottom+2  
    snakeRect.insert(0,head);  
    if head.right<0 or head.left>WINDOWWIDTH or head.bottom<0 or head.top>WINDOWHEIGHT:  
        break  
    if food.left == snakeRect[0].left-1 and food.top == snakeRect[0].top-1:  
        food.left = random.randint(0,WINDOWWIDTH/20-1)*(rectLength+2)  
        food.top = random.randint(0,WINDOWHEIGHT/20-1)*(rectLength+2)  
        pickUpSound.play()  
    else:  
         snakeRect.pop(len(snakeRect)-1)  
    windowSurface.fill(BLACK)  
    for i in range(len(snakeRect)):  
        pygame.draw.rect(windowSurface,GREEN,snakeRect[i])  
    windowSurface.blit(foodImage,food)  
    if food.left == 0 and food.right == 0:  
        i = 3  
    pygame.display.update()  
    mainClock.tick(10)      
