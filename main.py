
import pygame
import math
import random
import PyInstaller
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
#background=pygame.image.load('background.png')
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#player
playerImg=pygame.image.load('player.png')
playerX=370
playerY=480
playerX_change=0
#enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(10)
#bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=4
bullet_state="ready"
score_value=0
font=pygame.font.Font("freesansbold.ttf",48)
textX=10
textY=10
over_text=pygame.font.Font("freesansbold.ttf",256)
# Function for viewing score on screen
def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(0,255,0))
    screen.blit(score,(x,y))

# Function for displaying game over
def game_over_text():
    over_text=font.render("GAME OVER",True,(255,0,0))
    screen.blit(over_text,(300,250))

# function to display the player on screen
def player(x,y):
    screen.blit(playerImg,(x,y))

# function to display the enemy on screen
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

# Functon to display the bullet on screen
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

# Function to find whether the collision occurs or not
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False

#game loop
running=True
while running:
    # baground color r,gbb set to 255 means white color
    screen.fill((255,255,255))
 #   screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                # to move player to the left side of the window
                playerX_change=-2
            if event.key==pygame.K_RIGHT:
                # to move player to the right side of the window
                playerX_change=2
            if event.key==pygame.K_SPACE:
                # space is pressed means bullet is ready to fire
                # space bar is relesed means bullet changes its phase to fire.
                if bullet_state=="ready":
                    #bullet_sound=mixer.sound('laser.wav')
                    #bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                pygameX_change=0
    playerX += playerX_change
    # boundary of player
    if playerX<=0:
        playerX=0
    if playerX>=736:
        playerX=736
    for i in range(num_of_enemies):
        if enemyY[i]>400:
            # above condition tells that enemy reaches
            # very near to player so game is over
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i]+= enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=1
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-1
            enemyY[i] +=enemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            #explosion_sound=mixer.sound('explosion.wav')
            #explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # when collision occurs score is incremented by 1 and that fired enemy is genarated at random location
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state=="fire":
        # to show the bullet movement on screen
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    player(playerX,playerY)
    show_score(textX,textY)
    # at each every time we have to update the screen
    # otherwise the changes made may not be visible on screen
    pygame.display.update()

