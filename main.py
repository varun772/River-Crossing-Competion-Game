import pygame
import random
import math
import time

from pygame.font import FontType
from pygame.ftfont import Font

# intialize pygame
pygame.init()

mykran=0
# screen
screen = pygame.display.set_mode((800, 960))

# title and icon
pygame.display.set_caption("MY GAME")
icon = pygame.image.load('iron.png')
pygame.display.set_icon(icon)

v_font= pygame.font.Font('freesansbold.ttf',50)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 896
playerX_change = 0
playerY_change = 0

#player2
player1Img = pygame.image.load('player.png')
player1X = 470
player1Y = 0
player1X_change = 0
player1Y_change = 0
# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 800))
    if i == 0:
     enemyY.append(128)
    if i == 1:
     enemyY.append(320)
    if i == 2:
     enemyY.append(512)
    if i == 3:
     enemyY.append(704)
    if i == 4:
     enemyY.append(896)
    enemyX_change.append(0)
    enemyY_change.append(0) 

# enemy moving
enemy1Img = []
enemy1X   = []
enemy1Y   = []
enemy1X_change =[]
enemy1Y_change =[]
no_of_enemies = 5
for i in range(num_of_enemies):
    enemy1Img.append(pygame.image.load('enemy1.png'))
    enemy1X.append(random.randint(0, 800))
    if i == 0:
     enemy1Y.append(32)
    if i == 1:
     enemy1Y.append(224)
    if i == 2:
     enemy1Y.append(416)
    if i == 3:
     enemy1Y.append(608)
    if i == 4:
     enemy1Y.append(800)

score = 0
scorec=0
score1=0
def player(x, y):
    screen.blit(playerImg, (x, y))

def player1(x,y):
    screen.blit(player1Img, (x,y))

def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))


def enemy1(x, y,i):
    screen.blit(enemy1Img[i], (x, y))


def iscollision(enemyX,enemyY,playerX,playerY):
    for i in range(num_of_enemies):
        distance=math.sqrt((math.pow(enemyX-playerX,2))+(math.pow(enemyY-playerY,2)))
        if distance <=64:
            return True
        else:
            return False  



def player_score(score12):
    score12_val = v_font.render("score of player2: "+ str(score12),True,(200,120,0))
    screen.blit(score12_val,(200, 300))
              
def player1_score1(score13):
    score13_val = v_font.render("score of player1:"+ str(score13),True,(100,140,123))
    screen.blit(score13_val,(100,400))
check=0
mykran=0
c=0
b=0
# game loop
running = True
while running:
    if check < 4: 
        if mykran%2 ==0:
            print("hi") 
            # colour of screen
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (0, 80, 0), (0, 0, 800, 128))
            pygame.draw.rect(screen, (0, 80, 0), (0, 192, 800, 128))
            pygame.draw.rect(screen, (0, 80, 0), (0, 384, 800, 128))
            pygame.draw.rect(screen, (0, 80, 0), (0, 576, 800, 128))
            pygame.draw.rect(screen,  (0, 80, 0), (0, 768, 800, 128))
            
            if mykran == 0:
                i=0
            for i in range(num_of_enemies):
                enemy1X[i] = (enemy1X[i] + 0.1) % 800
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if keeystroke is pressed check whether it is left or right
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -20
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 20
                    if event.key == pygame.K_UP:
                        playerY_change = -20
                    if event.key == pygame.K_DOWN:
                        playerY_change = 20
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        playerY_change = 0
                playerX += playerX_change
                playerY += playerY_change

                if playerX <= 0:
                    playerX = 0
                elif playerX >= 736:
                    playerX = 736
                if playerY <= 0:
                    playerY = 0
                if playerY >= 896:
                    playerY = 896
            if 960 >playerY > 896:
                score = 0
            if 896 > playerY > 832:
                score = 10
            if 832 > playerY > 768:
                score = 20
            if 768 > playerY > 704:
                score = 30
            if 704 > playerY > 640:
                score = 40
            if 640 > playerY > 576:
                score =  50
            if 576 > playerY > 512:
                score = 60
            if 512 > playerY > 448:
                score = 70
            if 448 > playerY > 384:
                score = 80
            if 384 > playerY > 320:
                score = 90
            if 320 > playerY > 256:
                score = 100
            if 256 > playerY > 192:
                score = 110
            if 192 > playerY > 128:
                score = 120
            if 128 > playerY > 64:
                score = 130
            if 64 > playerY > 0:
                score = 140                                                              
            for i in range(num_of_enemies):
                collision=iscollision(enemyX[i],enemyY[i],playerX,playerY)
                if collision:
                    scorec += 1
                if scorec > 0:
                    mykran += 1
                    b=1
            for i in range(num_of_enemies):
                collision=iscollision(enemy1X[i],enemy1Y[i],playerX,playerY)
                if collision:
                    scorec += 1
                if scorec > 0:
                    b=1
                    mykran += 1              

            player(playerX, playerY)
            for i in range(num_of_enemies):    
                enemy(enemyX[i], enemyY[i],i)
            for i in range(num_of_enemies):
                enemy1(enemy1X[i], enemy1Y[i],i)
            if b == 1:
                screen.fill((100,100,100))
                player_score(score)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
        else:
            print("hey")
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (0, 80, 0), (0, 0, 800, 128))
            pygame.draw.rect(screen, (0, 80, 0), (0, 192, 800, 128))
            pygame.draw.rect(screen, (0, 80, 0), (0, 384, 800, 128))
            pygame.draw.rect(screen, (0, 80, 0), (0, 576, 800, 128))
            pygame.draw.rect(screen,  (0, 80, 0), (0, 768, 800, 128))
            if mykran == 0:
                i=0
            for i in range(num_of_enemies):
                enemy1X[i] = (enemy1X[i] + 0.1) % 800
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if keeystroke is pressed check whether it is left or right
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1X_change = -20
                    if event.key == pygame.K_RIGHT:
                        player1X_change = 20
                    if event.key == pygame.K_UP:
                        player1Y_change = -20
                    if event.key == pygame.K_DOWN:
                        player1Y_change = 20
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        playerY_change = 0
                player1X += player1X_change
                player1Y += player1Y_change

                if player1X <= 0:
                    player1X = 0
                elif player1X >= 736:
                    player1X = 736
                if player1Y <= 0:
                    player1Y = 0
                if player1Y >= 896:
                    player1Y = 896
            if 960 >player1Y > 896:
                score1 = 140
            if 896 > player1Y > 832:
                score1 = 130
            if 832 > player1Y > 768:
                score1 = 120
            if 768 > player1Y > 704:
                score1 = 110
            if 704 > player1Y > 640:
                score1 = 100
            if 640 > player1Y > 576:
                score1 = 90
            if 576 > player1Y > 512:
                score1 = 80
            if 512 > player1Y > 448:
                score1 = 70
            if 448 > player1Y > 384:
                score1 = 60
            if 384 > player1Y > 320:
                score1 = 50
            if 320 > player1Y > 256:
                score1 = 40
            if 256 > player1Y > 192:
                score1 = 30
            if 192 > player1Y > 128:
                score1 = 20
            if 128 > player1Y > 64:
                score1 = 10
            if 64 > player1Y > 0:
                score1 = 0                
            pygame.display.update()                                            
            for i in range(num_of_enemies):
                collision=iscollision(enemyX[i],enemyY[i],player1X,player1Y)
                if collision:
                    scorec += 1
                    mykran = 0
                if scorec > 0:
                    c = 1
                    mykran += 1
            for i in range(num_of_enemies):
                collision=iscollision(enemy1X[i],enemy1Y[i],player1X,player1Y)
                if collision:
                    scorec += 1
                    mykran = 0
                if scorec > 0:
                    c = 1
                    mykran += 1
            print("rely")
            player1(player1X, player1Y)
            for i in range(num_of_enemies):    
                enemy(enemyX[i], enemyY[i],i)
            for i in range(num_of_enemies):
                enemy1(enemy1X[i], enemy1Y[i],i)
        if c == 1:
                screen.fill((100,100,100))
                player1_score1(score1)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
    pygame.display.update()
