import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

brush_size = 5
current_color = BLACK
mode = "pen"  

screen.fill(WHITE)

def draw_circle(start_pos, end_pos, color):
    radius = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1])) // 2
    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
    pygame.draw.circle(screen, color, center, radius, 2)

def draw_rectangle(start_pos, end_pos, color):
    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                       abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    pygame.draw.rect(screen, color, rect, 2)

def draw_square(start_pos, end_pos, color):
    side_length = min(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    top_left = (min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]))
    pygame.draw.rect(screen, color, pygame.Rect(top_left, (side_length, side_length)), 2)

def draw_right_triangle(start_pos, end_pos, color):
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    points = [
        start_pos,
        (start_pos[0] + width, start_pos[1]),
        (start_pos[0], start_pos[1] + height)
    ]
    pygame.draw.polygon(screen, color, points, 2)

def draw_equilateral_triangle(start_pos, end_pos, color):
    side_length = min(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    height = math.sqrt(3) * side_length / 2
    top_x = (start_pos[0] + end_pos[0]) // 2
    top_y = min(start_pos[1], end_pos[1]) - height
    points = [
        (top_x, top_y),
        (start_pos[0], start_pos[1]),
        (end_pos[0], end_pos[1])
    ]
    pygame.draw.polygon(screen, color, points, 2)

def draw_rhombus(start_pos, end_pos, color):
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    center_x = (start_pos[0] + end_pos[0]) // 2
    center_y = (start_pos[1] + end_pos[1]) // 2
    points = [
        (center_x, start_pos[1]),
        (start_pos[0], center_y),
        (center_x, end_pos[1]),
        (end_pos[0], center_y)
    ]
    pygame.draw.polygon(screen, color, points, 2)

running = True
drawing = False
start_pos = (0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if mode == "pen":
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)
                elif mode == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size)

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if mode == "rect":
                draw_rectangle(start_pos, end_pos, current_color)
            elif mode == "circle":
                draw_circle(start_pos, end_pos, current_color)
            elif mode == "square":
                draw_square(start_pos, end_pos, current_color)
            elif mode == "right_triangle":
                draw_right_triangle(start_pos, end_pos, current_color)
            elif mode == "equilateral_triangle":
                draw_equilateral_triangle(start_pos, end_pos, current_color)
            elif mode == "rhombus":
                draw_rhombus(start_pos, end_pos, current_color)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_q:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_p:
                mode = "pen"

            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE

    pygame.display.flip()

pygame.quit()
