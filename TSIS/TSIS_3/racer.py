import pygame, random

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()                      # initializing the Sprite base class
        self.image = image                      # object image
        self.rect = self.image.get_rect(center=(x, y))  # rectangle for position and collisions

class Enemy(GameObject):
    def __init__(self, image, speed, width):
        # creating an enemy in a random position on the X-axis, on top of the screen
        super().__init__(image, random.randint(50, width-50), -100)
        self.speed = speed                      # Enemy movement speed
    
    def update(self):
        # updating the enemy's position (moving down)
        self.rect.y += self.speed