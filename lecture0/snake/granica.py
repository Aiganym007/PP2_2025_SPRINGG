'''
import pygame
import random
from color import *
pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0 
        self.score = 0
        self.level = 1

    def move(self):
        head = self.body[0]
        new_head = Point(head.x + self.dx, head.y + self.dy)

        # Check for collision with the boundaries
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return False  # Snake hit the boundary, game over
        
        # Check for collision with itself
        if new_head in self.body:
            return False  # Snake hit itself, game over
        
        # Move the snake
        self.body.insert(0, new_head)
        self.body.pop()
        return True

    def draw(self):
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0] == food.pos:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  
            self.score += 1

            if self.score % 3 == 0:  
                self.level += 1

            food.generate_random_pos(self)  
            return True
        return False

class Food:
    def __init__(self, food_type="regular"):
        self.pos = Point(0, 0)
        self.food_type = food_type  # Define whether it's regular food or boundary food
        self.generate_random_pos(None)  

    def generate_random_pos(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            new_pos = Point(x, y)
            if snake is None or new_pos not in snake.body:
                self.pos = new_pos
                break

    def draw(self):
        if self.food_type == "regular":
            pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Green food
        elif self.food_type == "boundary":
            pygame.draw.rect(screen, colorBLUE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Blue food

# Initialize snake and food
snake = Snake()
food_regular = Food("regular")
food_boundary = Food("boundary")

FPS = 4  
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(colorBLACK)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    if not snake.move():
        running = False  # Game over if the snake collides with the boundary or itself

    # Check if snake eats regular food or boundary food
    if snake.check_collision(food_regular):
        pass  # Game continues if snake eats regular food
    elif snake.check_collision(food_boundary):
        running = False  # End game if snake eats boundary food

    snake.draw()
    food_regular.draw()
    food_boundary.draw()

    score_text = font.render(f"Score: {snake.score}", True, colorWHITE)
    level_text = font.render(f"Level: {snake.level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    
    clock.tick(FPS + snake.level)  

# Game over screen
screen.fill(colorBLACK)

game_over_text = game_over_font.render("GAME OVER", True, colorRED)
text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
screen.blit(game_over_text, text_rect)

final_score_text = font.render(f"Final Score: {snake.score}", True, colorWHITE)
score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
screen.blit(final_score_text, score_rect)

final_level_text = font.render(f"Final Level: {snake.level}", True, colorWHITE)
level_rect = final_level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
screen.blit(final_level_text, level_rect)

pygame.display.flip()
pygame.time.delay(3000) 

pygame.quit()
'''

import pygame
import random
from color import *
pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0 
        self.score = 0
        self.level = 1

    def move(self):
        head = self.body[0]
        new_head = Point(head.x + self.dx, head.y + self.dy)

        # Check for collision with the boundaries
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return False  # Snake hit the boundary, game over
        
        # Check for collision with itself
        if new_head in self.body:
            return False  # Snake hit itself, game over
        
        # Move the snake
        self.body.insert(0, new_head)
        self.body.pop()
        return True

    def draw(self):
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0] == food.pos:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  
            self.score += 1

            if self.score % 3 == 0:  
                self.level += 1

            food.generate_random_pos(self)  
            return True
        return False

class Food:
    def __init__(self, food_type="regular", pos=None):
        self.pos = pos if pos else Point(0, 0)
        self.food_type = food_type  # Define whether it's regular food or boundary food

    def generate_random_pos(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            new_pos = Point(x, y)
            if snake is None or new_pos not in snake.body:
                self.pos = new_pos
                break

    def draw(self):
        if self.food_type == "regular":
            pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Green food
        elif self.food_type == "boundary":
            pygame.draw.rect(screen, colorBLUE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Blue food

# Initialize snake and food
snake = Snake()
food_regular = Food("regular")

# Fixed boundary food at the center (one cell)
boundary_food = Food("boundary", Point(WIDTH // CELL // 2, HEIGHT // CELL // 2))  # Only one food at the center

FPS = 4  
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(colorBLACK)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    if not snake.move():
        running = False  # Game over if the snake collides with the boundary or itself

    # Check if snake eats regular food
    if snake.check_collision(food_regular):
        pass  # Game continues if snake eats regular food

    # Check if snake eats boundary food (game over)
    if snake.check_collision(boundary_food):
        running = False  # End game if snake eats the boundary food

    snake.draw()
    food_regular.draw()
    boundary_food.draw()  # Draw the blue boundary food

    score_text = font.render(f"Score: {snake.score}", True, colorWHITE)
    level_text = font.render(f"Level: {snake.level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    
    clock.tick(FPS + snake.level)  

# Game over screen
screen.fill(colorBLACK)

game_over_text = game_over_font.render("GAME OVER", True, colorRED)
text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
screen.blit(game_over_text, text_rect)

final_score_text = font.render(f"Final Score: {snake.score}", True, colorWHITE)
score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
screen.blit(final_score_text, score_rect)

final_level_text = font.render(f"Final Level: {snake.level}", True, colorWHITE)
level_rect = final_level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
screen.blit(final_level_text, level_rect)

pygame.display.flip()
pygame.time.delay(3000) 

pygame.quit()



