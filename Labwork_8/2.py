import random
import pygame, time

pygame.init()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 600))
background = pygame.transform.smoothscale(pygame.image.load('bk2.jpg'), (800, 600))
pygame.display.set_caption('SNAKE GAME')

font = pygame.font.SysFont('Verdana', 60)
game_over = font.render("Game Over", True, RED)
font1 = pygame.font.SysFont('Verdana', 14)
levele = font1.render("LEVEL = ", True, BLACK)
scoree = font1.render("SCORE = ", True, BLACK)

class Snake:
    global level, score
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
        self.radius = 10
        self.dx = 5  # Right.
        self.dy = 0
        self.is_add = False
        self.speed = 30

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, BLACK, element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if score % 5 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if self.elements[0][0] > 790 or self.elements[0][0] < 20:
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play()
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            pygame.exit()

        if self.elements[0][1] > 580 or self.elements[0][1] < 20:
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play()
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            pygame.exit()

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False

class Food:
    def __init__(self):
        self.x = random.randint(30, 670)
        self.y = random.randint(30, 470)

    def gen(self):
        self.x = random.randint(30, 670)
        self.y = random.randint(30,470)

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 10, 10))

score = 0
level = 0
def show_level(x, y):
    global level
    s = font1.render(f'{level}', True, BLACK)
    screen.blit(s, (x, y))
def show_score(x, y):
    global score
    s = font1.render(f'{score}', True, BLACK)
    screen.blit(s, (x, y))

snake1 = Snake(100, 100)
food = Food()

running = True
FPS = 30
d = 5

clock = pygame.time.Clock()

while running:
    clock.tick(snake1.speed)
    show_score(795, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d


    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        score += 1
        pygame.mixer.Sound('food.mp3').play()
        food.gen()
        # passes new level
        if score % 5 == 0:
            pygame.mixer.Sound('newlevel.mp3').play()
            level += 1

    snake1.move()
    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    snake1.draw()
    food.draw()
    screen.blit(levele, (700, 40))
    screen.blit(scoree, (700, 20))
    show_score(775, 20)
    show_level(770, 40)
    # pygame.draw.line(screen, RED, (5, 5), (795, 5), 3)
    pygame.draw.rect(screen, RED, (5, 5, 790, 580), 3)
    pygame.display.update()

pygame.quit()