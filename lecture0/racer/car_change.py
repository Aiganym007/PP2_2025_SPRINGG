import pygame
from pygame.locals import *
import random, time
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
W, H = 400, 600  
Speed = 5  
SCORE = 0  
n = 5 

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

background = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\AnimatedStreet.png")

scr = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")

crash_sound = pygame.mixer.Sound(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\crash.wav')
coin_sound = pygame.mixer.Sound(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\catch.mp3')

pygame.mixer.music.load(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\bck.wav.wav')
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def update(self):
        self.rect.move_ip(0, Speed)
        if self.rect.bottom > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.original_image = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\Player.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def update(self):
        pressed_keys = pygame.key.get_pressed() 
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < W and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if pressed_keys[K_r]:
            new_car = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\car.png")  
            self.image = pygame.transform.scale(new_car, (70, 120)) 
        elif pressed_keys[K_p]:
            self.image = self.original_image

class Coin(pygame.sprite.Sprite):
    def __init__(self, image_path, score_value):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W-40), 530)
        self.score = score_value  

    def change(self):
        self.rect.center = (random.randint(40,W-40), 530)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)

def spawn_new_coin():
    coin_types = [
        (r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\coin1.png", 0.5),
        (r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\coin2.png", 1),
        (r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lecture0\racer\gem.png", 1.5)
    ]
    
    image_path, score_value = random.choice(coin_types)
    new_coin = Coin(image_path, score_value)
    
    coins.add(new_coin)
    all_sprites.add(new_coin)
    return new_coin

current_coin = spawn_new_coin()

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == INC_SPEED:
            Speed += 0.5 

    scr.blit(background, (0, 0))

    scores = font_small.render(f"Score: {SCORE}", True, "black")
    scr.blit(scores, (10, 10))

    for entity in all_sprites:
        entity.update()
        scr.blit(entity.image, entity.rect)   

    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        time.sleep(1)

        scr.fill("red")
        scr.blit(game_over, (30, 250))
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill()

        time.sleep(3)
        pygame.quit()
        exit()

    collected_coin = pygame.sprite.spritecollideany(P1, coins)  

    if collected_coin:
        coin_sound.play()

        SCORE += collected_coin.score 
        coins.remove(collected_coin)  
        all_sprites.remove(collected_coin)  

        current_coin = spawn_new_coin()

        if SCORE >= n:
            Speed += 1
            n += 5  

    pygame.display.flip()
    FramePerSec.tick(FPS)
