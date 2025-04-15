import pygame
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

def draw_line(start_pos, end_pos, color, size):
    if start_pos[0] == end_pos[0]:  
        pygame.draw.line(screen, color, start_pos, end_pos, size)
    elif start_pos[1] == end_pos[1]:
        pygame.draw.line(screen, color, start_pos, end_pos, size)

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
                    end_pos = event.pos
                    if start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]: 
                        draw_line(start_pos, end_pos, current_color, brush_size)
                elif mode == "eraser":
                    end_pos = event.pos
                    if start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]:  
                        draw_line(start_pos, end_pos, WHITE, brush_size)

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if mode == "pen":
                if start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]:
                    draw_line(start_pos, end_pos, current_color, brush_size)
            elif mode == "eraser":
                if start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]:
                    draw_line(start_pos, end_pos, WHITE, brush_size)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"

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
