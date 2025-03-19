import pygame
from pygame.locals import *
import random
import time
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
W = 400
H = 600
Speed = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")
sco = font_small.render("Your score was", True, "black")

background = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab8\racer\AnimatedStreet.png")

scr = pygame.display.set_mode((400,600))
scr.fill("white")
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab8\racer\en.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W-40), 0)

      def move(self):
        self.rect.move_ip(0,Speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab8\racer\pl.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < W:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab8\racer\coin1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W-40), 530)

    def move(self):
        global SCORE

    def change(self):
        self.rect.center = (random.randint(40,W-40), 530)
         
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:    
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              Speed += 0.5      
        if event.type == pygame.QUIT:
            exit()
   
    scr.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, "black")
    scr.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        scr.blit(entity.image, entity.rect)
  
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab8\racer\crash.wav').play()
          time.sleep(1)
                   
          scr.fill("red")
          scr.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites: 
                entity.kill() 
          time.sleep(4)
          pygame.quit() 
          exit() 

    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab8\racer\catch.mp3').play()

        SCORE += 1
        C1.change()
           
    pygame.display.flip()
    FramePerSec.tick(FPS)