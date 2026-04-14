import pygame
import clock

pygame.init()

screen = pygame.display.set_mode((500, 400))
clock.load_images()
pygame.display.set_caption("Mickey Clock")

clock_fps = pygame.time.Clock()
done = False

background = pygame.image.load("Clock.jpeg")
background = pygame.transform.scale(background, (500, 400))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, (0, 0))

    clock.draw_hands(screen)
    
    pygame.display.flip()
    clock_fps.tick(60)

pygame.quit()