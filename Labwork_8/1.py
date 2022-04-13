import pygame, random
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 600))

def enemy(x, y, IMG, d):
    screen.blit(IMG, (x, y))
    y += d
ok = True

def collision(x1, x2, y1, y2):
    global ok
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if d <= 40:
        ok = False
        return True
    else:
        return False
restart = False

#game over
over_font = pygame.font.SysFont('Verdana', 50)
bgIMG = pygame.image.load('AnimatedStreet.png')

# player
playerIMG = pygame.image.load('Player.png')

# enemy
enemyIMG = pygame.image.load('Enemy.png')

#sound
def playbg():
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play(-1)
def crashMUS():
    crash = pygame.mixer.Sound('crash.wav')
    crash.play()
    
#score
score = 0
score_font = pygame.font.SysFont('Verdana', 35)
def show_score(x, y):
    global score
    s = score_font.render(f'{score}', True, (0, 0, 255))
    screen.blit(s, (x, y))
coinIMG = pygame.transform.smoothscale(pygame.image.load('coin.png'), (50,50))
def coin(x, y):
    screen.blit(coinIMG, (x, y))
ok = True
def main():
    global score
    score = 0
    playbg()
    coinX, coinY = random.randint(0, 352), 0
    coin_speed = 2.5
    enemyX, enemyY = random.randint(0, 352), 0
    enemy_speed = 2.5
    player_change = 0
    playerX, playerY = 178, 500
    while not collision(playerX, enemyX, playerY, enemyY):
        screen.blit(bgIMG, (0, 0))
        show_score(370, 50)
        enemyY += enemy_speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player_change = 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player_change = -3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_change = 0
        screen.blit(playerIMG, (playerX, playerY))
        playerX += player_change
        coinY += coin_speed
        if playerX <= 0:
            playerX = 0
        if playerX >= 356:
            playerX = 356
        if enemyY >= 600:
            enemyY = 0
            enemyX = random.randint(0, 352)
        if coinY >= 600:
            coinY = 0
            coinX = random.randint(0, 352)
        if collision(playerX, coinX, playerY, coinY):
            score += 1
            coinY = 0
            coinX = random.randint(0, 352)
        if collision(playerX, enemyX, playerY, enemyY):
            crashMUS()
        enemy(enemyX, enemyY, enemyIMG, enemy_speed)
        coin(coinX, coinY)
        pygame.display.update()
#game over and restart
def game_over(x, y):
    global ok, score
    s = over_font.render("GAME OVER", True, (0, 0, 0))
    sc = score_font.render('Your score: ', True, (0, 0, 0))
    re = score_font.render('Press F to restart', True, (0, 0, 0))
    while not ok:
        screen.fill('red')
        screen.blit(s, (x, y))
        screen.blit(sc, (x, y+50))
        show_score(x+200, y+50)
        screen.blit(re, (x, y+100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    ok = True
                    main()
        pygame.display.update()
main()
game_over(70, 200)