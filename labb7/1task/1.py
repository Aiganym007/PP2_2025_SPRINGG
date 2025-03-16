import pygame
import datetime
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\labb7\1task\mainclock.jpeg")  
right_hand = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\labb7\1task\rrrr.jpeg").convert() 
right_hand.set_colorkey((0, 0, 0)) 
left_hand = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\labb7\1task\lllllll.jpeg").convert()
left_hand.set_colorkey((0, 0, 0))

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
right_hand = pygame.transform.scale(right_hand, (700, 350))  
left_hand = pygame.transform.scale(left_hand, (700, 350))  
center_x, center_y = WIDTH // 2, HEIGHT // 2

def rotate_hand(i, a, length):
    rot_image = pygame.transform.rotate(i, a)
    rect = rot_image.get_rect(center=(center_x, center_y))
    return rot_image, rect

r = True
clock = pygame.time.Clock()
while r:
    screen.fill((255, 255, 255))  
    screen.blit(background, (0, 0))

    now = datetime.datetime.now()
    minute_a = -(now.minute * 6)  
    second_a = -(now.second * 6)  

    rot_right, right_rect = rotate_hand(right_hand, minute_a, 100)
    rot_left, left_rect = rotate_hand(left_hand, second_a, 120)

    screen.blit(rot_right, right_rect.topleft)
    screen.blit(rot_left, left_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30)  

pygame.quit()
