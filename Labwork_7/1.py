import pygame, datetime

pygame.init()

screen = pygame.display.set_mode((800,600))
back = pygame.transform.scale(pygame.image.load('mickeybg.jpeg'), (800,600))
sec = pygame.transform.smoothscale(pygame.image.load('mickeym.png'), (800,600))
min = pygame.transform.smoothscale(pygame.image.load('mickeyh.png'), (800,600))
hour = pygame.transform.smoothscale(pygame.image.load('mickeyh2.png'), (800,600))

clock = pygame.time.Clock()

def center(s, image, angle, x, y): 
    r_image = pygame.transform.rotate(image, angle) 
    n_rect = r_image.get_rect(center = image.get_rect(center = (x, y)).center) 
    s.blit(r_image,n_rect)
run = True
while run:
    screen.blit(back, (0,0))
    time = datetime.datetime.now()
    clock.tick(30)
    center(screen,sec,-time.second*6,400,300)
    center(screen,min,-time.minute*6,400,300)
    center(screen,hour,-time.hour*6,400,300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()