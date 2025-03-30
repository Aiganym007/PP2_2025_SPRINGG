import pygame
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Константы игры
FPS = 60
FramePerSec = pygame.time.Clock()
W, H = 400, 600  # Размеры окна
Speed = 5  # Начальная скорость врага
SCORE = 0  # Очки игрока
n = 5  # Количество очков для увеличения скорости

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

# Фон
background = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\AnimatedStreet.png")

# Создание окна
scr = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")

# Загрузка звуков
crash_sound = pygame.mixer.Sound(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\crash.wav')
coin_sound = pygame.mixer.Sound(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\catch.mp3')

pygame.mixer.music.load(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\bck.wav.wav')
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def update(self):
        """Двигает врага вниз и сбрасывает его наверх при выходе за пределы экрана."""
        self.rect.move_ip(0, Speed)
        if self.rect.bottom > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def update(self):
        """Обрабатывает управление игрока стрелками."""
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < W and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self, image_path, score_value):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W-40), 530)
        self.score = score_value  

    def change(self):
        """Перемещает монету в случайное место."""
        self.rect.center = (random.randint(40,W-40), 530)

# Создание объектов игрока и врага
P1 = Player()
E1 = Enemy()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)

# Функция создания новой случайной монеты
def spawn_new_coin():
    coin_types = [
        (r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\coin1.png", 0.5),
        (r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\coin2.png", 1),
        (r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab9\racer\gem.png", 1.5)
    ]
    
    image_path, score_value = random.choice(coin_types)
    new_coin = Coin(image_path, score_value)
    
    coins.add(new_coin)
    all_sprites.add(new_coin)
    return new_coin

# Создаём первую монету
current_coin = spawn_new_coin()

# Увеличение скорости каждые 1000 мс (1 сек)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == INC_SPEED:
            Speed += 0.5  # Постепенное увеличение скорости врага

    # Отрисовка фона
    scr.blit(background, (0, 0))

    # Отображение очков
    scores = font_small.render(f"Score: {SCORE}", True, "black")
    scr.blit(scores, (10, 10))

    # Движение и отрисовка всех спрайтов
    for entity in all_sprites:
        entity.update()
        scr.blit(entity.image, entity.rect)   

    # Столкновение с врагом — игра окончена
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

    # Столкновение с монетой
    collected_coin = pygame.sprite.spritecollideany(P1, coins)  # Проверяем, собрал ли игрок монету

    if collected_coin:
        coin_sound.play()

        SCORE += collected_coin.score  # Добавляем стоимость монеты к очкам
        coins.remove(collected_coin)  # Удаляем монету из группы
        all_sprites.remove(collected_coin)  # Удаляем монету из всех спрайтов

        # Создаём новую монету
        current_coin = spawn_new_coin()

        # Увеличение скорости при достижении порога n очков
        if SCORE >= n:
            Speed += 1
            n += 5  # Следующий порог увеличения скорости

    pygame.display.flip()
    FramePerSec.tick(FPS)
