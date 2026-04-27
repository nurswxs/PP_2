import pygame, random, sys

pygame.init()

# Screen parametrs
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game Extended")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

import os
os.chdir(os.path.dirname(__file__)) 
# Catalog of works main.py on-site installation

# Download image
road = pygame.image.load("image/background.png")
car = pygame.image.load("image/player.png")
enemy = pygame.image.load("image/enemy.png")
coin = pygame.image.load("image/coin.png")

# Change size
road = pygame.transform.scale(road, (WIDTH, HEIGHT))
car = pygame.transform.scale(car, (50, 100))
enemy = pygame.transform.scale(enemy, (50, 100))
coin = pygame.transform.scale(coin, (30, 30))

# My car
player_rect = car.get_rect(center=(WIDTH//2, HEIGHT-100))

# enemy car
enemy_rect = enemy.get_rect(center=(random.randint(50, WIDTH-50), -100))
enemy_speed = 5

# Coin (with different weights)
def random_coin():
    rect = coin.get_rect(center=(random.randint(50, WIDTH-50), -50))
    weight = random.choice([1, 2, 5])  # coin weight (point value)
    return rect, weight

coin_rect, coin_weight = random_coin()

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    screen.blit(road, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controlling my car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

    # Enemy moving car
    enemy_rect.y += enemy_speed
    if enemy_rect.top > HEIGHT:
        enemy_rect.center = (random.randint(50, WIDTH-50), -100)

    # Coin moving 
    coin_rect.y += 5
    if coin_rect.top > HEIGHT:
        coin_rect, coin_weight = random_coin()

    # Collision
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(coin_rect):
        score += coin_weight  # Points are added depending on the weight of the coin.
        coin_rect, coin_weight = random_coin()

        # Enemy speed increases when collecting N coins
        if score % 10 == 0:  # speed increases every 10 points
            enemy_speed += 1

    # Draw
    screen.blit(car, player_rect)
    screen.blit(enemy, enemy_rect)
    screen.blit(coin, coin_rect)

    # Show Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)