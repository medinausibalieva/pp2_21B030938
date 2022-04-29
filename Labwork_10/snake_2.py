import psycopg2
import random
import pygame, time

pygame.init()

username = input()
score = 0
level = 1

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='21B030938'
)

sql = """
SELECT exists(select 1 from game where username=%s)
"""
cur = conn.cursor()
cur.execute(sql, (username,))
result = cur.fetchone()
if result[0]:
    sql = "select level from game where username = %s"
    cur.execute(sql, (username,))
    num = cur.fetchone()
    level = num[0]
else:
    sql = "insert into game (username, level) values (%s, %s)"
    cur.execute(sql, (username, level))
    conn.commit()

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)
background = pygame.transform.smoothscale(pygame.image.load('bk2.jpg'), (800, 600))
pygame.display.set_caption('SNAKE')
clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 60)
game_over = font.render("Game Over", True, RED)
font1 = pygame.font.SysFont('Verdana', 14)
levele = font1.render("LEVEL = ", True, BLACK)
scorere = font1.render("SCORE = ", True, BLACK)

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
        # collision with walls
        if self.elements[0][0] > 715 or self.elements[0][0] < 45:
            sql = """
                update game
                set level = %s
                where username = %s;
                """
            cur.execute(sql, (level, username))
            conn.commit()
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play()
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()

        if self.elements[0][1] > 515 or self.elements[0][1] < 45:
            sql = """
                update game
                set level = %s
                where username = %s;
                """
            cur.execute(sql, (level, username))
            conn.commit()
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play()
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        # for big food
        if score % 10 == 0 and score != 0:
            if foodx <= x <= foodx + 20 and foody <= y <= foody + 20:
                return True
            return False
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False


class Food:
    global score, level
    def __init__(self):
        self.x = random.randint(50, 620)
        self.y = random.randint(50, 420)

    def gen(self):
        self.x = random.randint(50, 620)
        self.y = random.randint(50, 420)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 10, 10))

class Food1:
    global score, level
    def __init__(self):
        self.x = random.randint(50, 620)
        self.y = random.randint(50, 420)

    def gen(self):
        self.x = random.randint(50, 620)
        self.y = random.randint(50, 420)

    def draw(self):
        if score % 10 == 0 and score != 0:
            pygame.draw.rect(screen, RED, (self.x, self.y, 20, 20))
# for level
def show_level(x, y):
    global level
    s = font1.render(f'{level}', True, BLACK)
    screen.blit(s, (x, y))
# for score
def show_score(x, y):
    global score
    s = font1.render(f'{score}', True, BLACK)
    screen.blit(s, (x, y))

snake1 = Snake(100, 100)
food = Food()
food1 = Food1()


running = True

FPS = 30
d = 5


while running:
    screen.fill(WHITE)
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(level)
            sql = """
                update game
                set level = %s
                where username = %s;
                """
            cur.execute(sql, (level, username))
            conn.commit()
            pygame.quit()
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
    if snake1.eat(food1.x, food1.y):
        snake1.is_add = True
        score += 3
        pygame.mixer.Sound('food.mp3').play()
        food1.gen()

    start_ticks = pygame.time.get_ticks()
    snake1.move()
    snake1.draw()
    food.draw()
    food1.draw()
    screen.blit(levele, (700, 0))
    screen.blit(scorere, (700, 20))
    pygame.draw.rect(screen, BLACK, (40, 40, 720, 520), 2)
    show_score(775, 20)
    show_level(770, 0)
    pygame.display.flip()

pygame.quit()