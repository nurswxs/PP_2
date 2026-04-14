import pygame
from ball import Ball, STEP

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball = Ball(WIDTH // 2, HEIGHT // 2)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move(-STEP, 0, WIDTH, HEIGHT)

            if event.key == pygame.K_RIGHT:
                ball.move(STEP, 0, WIDTH, HEIGHT)

            if event.key == pygame.K_UP:
                ball.move(0, -STEP, WIDTH, HEIGHT)

            if event.key == pygame.K_DOWN:
                ball.move(0, STEP, WIDTH, HEIGHT)

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()