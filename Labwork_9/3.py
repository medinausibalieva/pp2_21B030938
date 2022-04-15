import pygame
import random
import math

pygame.init()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 600))
screen.fill((BLACK))
base_layer = pygame.Surface((800, 600))

draw_on = False
figure = False
figure_type = None

pos_last = (0, 0)
thickness = 1

color = GREEN
done = False
figure_type = 'pen'
erase = False

def Rect_pos(x1, y1, x2, y2): 
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) 

while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = BLUE
            if event.key == pygame.K_2:
                color = GREEN
            if event.key == pygame.K_3:
                color = RED
            if event.key == pygame.K_4:
                color = WHITE    
            if event.key == pygame.K_r:
                figure_type = 'rectangle'
            if event.key == pygame.K_p:
                figure_type = 'pen'
            if event.key == pygame.K_e:
                figure_type = 'erase'
            if event.key == pygame.K_c:
                figure_type = 'circle'
            if event.key == pygame.K_s:
                figure_type = 'square'    
            if event.key == pygame.K_t:
                figure_type = 'right triangle'    
            if event.key == pygame.K_q:
                figure_type = 'equilateral triangle'    
            if event.key == pygame.K_h:
                figure_type = 'rhombus'
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_on = True
            pos_last = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            base_layer.blit(screen, (0, 0))
            draw_on = False
            
        if event.type == pygame.MOUSEMOTION:
            if draw_on:
                if figure_type == 'circle':
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.circle(screen, color, (pos_last[0], pos_last[1]), int(math.sqrt((event.pos[0]-pos_last[0])**2 + (event.pos[1]-pos_last[1])**2)))
                if figure_type == 'rectangle':
                    t = Rect_pos(pos_last[0], pos_last[1], event.pos[0], event.pos[1])
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.rect(screen, color, pygame.Rect(t))
                if figure_type == 'pen':
                    pygame.draw.line(screen, color, [pos_last[0], pos_last[1]], [event.pos[0], event.pos[1]], 2)
                    pos_last = event.pos
                if figure_type == 'erase':
                    pygame.draw.circle(screen, (0, 0, 0), (event.pos[0], event.pos[1]), 9)
                if figure_type == 'square':
                    t = Rect_pos(pos_last[0], pos_last[0], event.pos[0], event.pos[0])
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.rect(screen, color, pygame.Rect(t))
                if figure_type == 'right triangle':
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.polygon(screen, color, [(pos_last[0], pos_last[1] + event.pos[0]), (pos_last[0], pos_last[1]), (pos_last[0] + 2 * event.pos[0], pos_last[1])])
                if figure_type == 'equilateral triangle':
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.polygon(screen, color, [(pos_last[0] - event.pos[0], pos_last[0] + event.pos[0]), (pos_last[0] + event.pos[0], pos_last[0] + event.pos[0]), (pos_last[0], pos_last[0] - event.pos[0])])
                if figure_type == 'rhombus':
                    pos1 = (pos_last[0] / 2, pos_last[1] / 2 - event.pos[0] / 2)
                    pos2 = (pos1[0] - event.pos[1] / 2, pos1[1] + event.pos[0] / 2)
                    pos3 = (pos1[0], pos1[1] + event.pos[0])
                    pos4 = (pos2[0] + event.pos[1], pos2[1])
                    points = [pos1, pos2, pos3, pos4]
                    screen.blit(base_layer, (0, 0))
                    pygame.draw.polygon(screen, color, points)
    pygame.display.flip()

pygame.quit()