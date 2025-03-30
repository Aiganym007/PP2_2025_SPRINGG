import pygame
import random
import time
from color import *

# Инициализация Pygame
pygame.init()

# Константы игры
WIDTH = 600
HEIGHT = 600
CELL = 30  # Размер одной клетки

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Шрифты
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

# Функция отрисовки сетки
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# Класс точки (ячейки змейки и еды)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0  # Движение вправо
        self.score = 0
        self.level = 1

    def move(self):
        """Перемещает змейку и проверяет столкновения"""
        head = self.body[0]
        new_head = Point(head.x + self.dx, head.y + self.dy)

        # Проверка на выход за границы
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return False
        
        # Проверка столкновения с собой
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)
        self.body.pop()
        return True

    def draw(self):
        """Отрисовка змейки"""
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        """Проверяет столкновение с едой"""
        if self.body[0] == food.pos:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  
            self.score += food.value  # Добавление очков
            if self.score % 3 == 0:  
                self.level += 1

            food.generate_random_pos(self)  # Генерация новой еды
            return True
        return False

# Класс еды
class Food:
    def __init__(self, image, value):
        # Загружаем изображение и изменяем его размер до размера клетки
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (CELL, CELL))  # Масштабируем изображение
        self.value = value  # Сколько очков даёт эта еда
        self.pos = Point(0, 0)
        self.generate_random_pos(None)  
        self.timer = time.time()  # Таймер для исчезновения еды

    def generate_random_pos(self, snake):
        """Генерирует случайную позицию для еды, избегая змейки"""
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            new_pos = Point(x, y)
            if snake is None or new_pos not in snake.body:
                self.pos = new_pos
                self.timer = time.time()  # Обновляем таймер
                break

    def draw(self):
        """Отрисовка еды"""
        screen.blit(self.image, (self.pos.x * CELL, self.pos.y * CELL))  # Отрисовываем еду с учётом масштаба

    def should_disappear(self):
        """Проверяет, должна ли еда исчезнуть (спустя 5 секунд)"""
        return time.time() - self.timer > 5

# Создание змейки и списка еды с разными очками
snake = Snake()
foods = [
    Food(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\snake\apple.png", 1),  
    Food(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\snake\banana.png", 2),  
    Food(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\snake\cherry.png", 3)  
]
current_food = random.choice(foods)  # Случайная еда

# Настройки игры
FPS = 4  
clock = pygame.time.Clock()
running = True

# Игровой цикл
while running:
    screen.fill(colorBLACK)
    draw_grid()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Управление змейкой
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    # Движение змейки и проверка на проигрыш
    if not snake.move():
        running = False  

    # Проверка съеденной еды
    if snake.check_collision(current_food):
        current_food = random.choice(foods)  # Выбираем новую еду
        current_food.generate_random_pos(snake)

    # Если еда исчезла по таймеру, генерируем новую
    if current_food.should_disappear():
        current_food = random.choice(foods)
        current_food.generate_random_pos(snake)

    # Отрисовка элементов
    snake.draw()
    current_food.draw()

    # Вывод счета и уровня
    score_text = font.render(f"Score: {snake.score}", True, colorWHITE)
    level_text = font.render(f"Level: {snake.level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS + snake.level)  # Скорость увеличивается с уровнем

# Отображение экрана "Game Over"
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
