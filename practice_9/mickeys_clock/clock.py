import pygame
import datetime

CENTER = (250, 220)

left_hand_img = None
right_hand_img = None


def load_images():
    global left_hand_img, right_hand_img

    left_hand_img = pygame.image.load("left_hand.jpg").convert_alpha()
    right_hand_img = pygame.image.load("right_hand.png").convert_alpha()

    left_hand_img = pygame.transform.scale(left_hand_img, (60, 240))  
    right_hand_img = pygame.transform.scale(right_hand_img, (70, 160)) 


def get_time_angles():
    now = datetime.datetime.now()
    return now.second * 6, now.minute * 6


def draw_hands(screen):
    sec_angle, min_angle = get_time_angles()

    left_hand = pygame.transform.rotate(left_hand_img, -sec_angle)
    right_hand = pygame.transform.rotate(right_hand_img, -min_angle)

    left_rect = left_hand.get_rect(center=CENTER)
    right_rect = right_hand.get_rect(center=CENTER)

    screen.blit(right_hand, right_rect)
    screen.blit(left_hand, left_rect)