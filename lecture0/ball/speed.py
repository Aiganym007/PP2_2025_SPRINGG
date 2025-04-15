import pygame
pygame.init()

w, h = 700, 700
White = (255, 255, 255)
speed = 5  # начальная скорость
max_speed = 20  # максимальная скорость
acceleration = 1.05  # коэффициент ускорения
RED = (255, 0, 0)
x, y = 350, 350

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()
    
    screen.fill(White)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y - 50 > 0:
        y -= speed
    if pressed[pygame.K_DOWN] and y + 50 < h:
        y += speed
    if pressed[pygame.K_LEFT] and x - 50 > 0:
        x -= speed
    if pressed[pygame.K_RIGHT] and x + 50 < w:
        x += speed

    if speed < max_speed:
        speed *= acceleration 

    pygame.draw.circle(screen, RED, (x, y), 50)

    pygame.display.flip()
    clock.tick(FPS)
