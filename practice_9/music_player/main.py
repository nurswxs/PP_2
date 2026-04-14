import pygame
import player

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            if event.key == pygame.K_s:
                player.stop()
            if event.key == pygame.K_n:
                player.next_track()
            if event.key == pygame.K_b:
                player.prev_track()
            if event.key == pygame.K_q:
                done = True

    if player.is_playing and not pygame.mixer.music.get_busy():
        player.next_track()

    screen.fill((255, 255, 255))

    track_text = font.render(f"Now playing: {player.get_track_name()}", True, (0,0,0))
    screen.blit(track_text, (50, 80))

    pos = player.get_position()
    time_text = font.render(f"Time: {pos}s", True, (0,0,0))
    screen.blit(time_text, (50, 130))

    controls = "P-Play  S-Stop  N-Next  B-Back  Q-Quit"
    controls_text = font.render(controls, True, (0,0,0))
    screen.blit(controls_text, (50, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()