import random

import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = width, height = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('PyGame Example')

clock = pygame.time.Clock()

x = 100
y = 100
change_x = 20
change_y = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= change_y
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += change_y
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= change_x
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += change_x

    
    if y > 450 or y < 0:
        change_y *= -1
    if x > 650 or x < 0:
        change_x *= -1    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= change_y
    if pressed[pygame.K_DOWN]: y += change_y
    if pressed[pygame.K_LEFT]: x -= change_x
    if pressed[pygame.K_RIGHT]: x += change_x

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, [x, y, 50, 50])
    clock.tick(30)
    pygame.display.update()