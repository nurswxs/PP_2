import pygame

RADIUS = 25
STEP = 20


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, screen_width, screen_height):
        new_x = self.x + dx
        new_y = self.y + dy

        if RADIUS <= new_x <= screen_width - RADIUS:
            self.x = new_x

        if RADIUS <= new_y <= screen_height - RADIUS:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), RADIUS)