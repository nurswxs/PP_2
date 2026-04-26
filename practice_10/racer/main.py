import pygame, random, sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for FPS
clock = pygame.time.Clock()

import os
os.chdir(os.path.dirname(__file__)) 

road = pygame.image.load("png/background.png")
car = pygame.image.load("png/player.png")
enemy = pygame.image.load("png/enemy.png")
coin = pygame.image.load("png/coin.png")


car = pygame.transform.scale(car, (50, 100))
enemy = pygame.transform.scale(enemy, (50, 100))
coin = pygame.transform.scale(coin, (30, 30))


player_rect = car.get_rect(center=(WIDTH//2, HEIGHT-100))


enemy_rect = enemy.get_rect(center=(WIDTH//2, -100))
enemy_speed = 5


coin_rect = coin.get_rect(center=(random.randint(50, WIDTH-50), -50))
coin_speed = 5
coins_collected = 0


font = pygame.font.SysFont("Arial", 24)


running = True
while running:
    screen.fill(WHITE)
    screen.blit(road, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5


    enemy_rect.y += enemy_speed
    if enemy_rect.top > HEIGHT:
        enemy_rect.center = (random.randint(50, WIDTH-50), -100)


    coin_rect.y += coin_speed
    if coin_rect.top > HEIGHT:
        coin_rect.center = (random.randint(50, WIDTH-50), -50)


    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(coin_rect):
        coins_collected += 1
        coin_rect.center = (random.randint(50, WIDTH-50), -50)


    screen.blit(car, player_rect)
    screen.blit(enemy, enemy_rect)
    screen.blit(coin, coin_rect)

    score_text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(score_text, (WIDTH-120, 20))


    pygame.display.update()
    clock.tick(60)