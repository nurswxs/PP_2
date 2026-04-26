import pygame, sys

pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program with Color Buttons")

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Бастапқы түс
current_color = BLACK

# Құралдар: 'brush', 'rect', 'circle', 'eraser'
tool = "brush"

clock = pygame.time.Clock()

# Түстерді таңдау батырмалары (экранның төменгі жағында)
color_buttons = {
    "black": pygame.Rect(10, HEIGHT-40, 30, 30),
    "red":   pygame.Rect(50, HEIGHT-40, 30, 30),
    "green": pygame.Rect(90, HEIGHT-40, 30, 30),
    "blue":  pygame.Rect(130, HEIGHT-40, 30, 30),
}

drawing = False
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Тышқан басу
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Егер батырмаға басылса – түс таңдау
            for name, rect in color_buttons.items():
                if rect.collidepoint(event.pos):
                    if name == "black": current_color = BLACK
                    elif name == "red": current_color = RED
                    elif name == "green": current_color = GREEN
                    elif name == "blue": current_color = BLUE
                    break
            else:
                drawing = True
                start_pos = event.pos

        # Тышқанды босату
        if event.type == pygame.MOUSEBUTTONUP:
            if tool == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
            elif tool == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
            drawing = False

        # Пернетақта арқылы құрал таңдау
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"

    # Сызу
    if drawing and tool == "brush":
        pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), 5)
    elif drawing and tool == "eraser":
        pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 10)

    # Түстер батырмаларын салу
    pygame.draw.rect(screen, BLACK, color_buttons["black"])
    pygame.draw.rect(screen, RED, color_buttons["red"])
    pygame.draw.rect(screen, GREEN, color_buttons["green"])
    pygame.draw.rect(screen, BLUE, color_buttons["blue"])

    pygame.display.update()
    clock.tick(60)