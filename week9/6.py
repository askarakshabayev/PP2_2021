import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))


class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5  # right
        self.dy = 0
        self.is_add = False
        self.speed = 30

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


snake = Snake()

running = True

d = 5

FPS = 30

clock = pygame.time.Clock()

k1_pressed = False

foodx = random.randint(0, 800)
foody = random.randint(0, 600)
food_rect = pygame.Rect(foodx, foody, 10, 10)

while running:
    mill = clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = d
            if event.key == pygame.K_1:
                snake.is_add = True
            if event.key == pygame.K_SPACE:
                snake.speed += 10

    head_x = snake.elements[0][0]
    head_y = snake.elements[0][1]
    if foodx + 10 >= head_x >= foodx and foody + 10 >= head_y >= foody:
        snake.is_add = True
        print("ttt")
    snake.move()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), food_rect)
    snake.draw()
    pygame.display.flip()