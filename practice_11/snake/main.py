import pygame, random, sys, time, os

pygame.init()

# Screen parametrs
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Images")

clock = pygame.time.Clock()

# Catalog of works main.py on-site installation
os.chdir(os.path.dirname(__file__))

# Download image
background = pygame.image.load("image/background.png")
snake_img = pygame.image.load("image/snake.png")
food_img = pygame.image.load("image/food.png")

# this part code change size
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
snake_img = pygame.transform.scale(snake_img, (CELL_SIZE, CELL_SIZE))
food_img = pygame.transform.scale(food_img, (CELL_SIZE, CELL_SIZE))

# Snake initial parameters
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# Food generation (with weight and timer)
def random_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            weight = random.choice([1, 2, 5])   # different weight
            expire_time = time.time() + 5       # Disappears after 5 seconds
            return (x, y), weight, expire_time

food, food_weight, food_timer = random_food()

# this is Score
score = 0
font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    screen.blit(background, (0, 0))  # Background image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controlling Snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # Moving Snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Hitting the wall
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("Game Over! Snake hit the wall.")
        pygame.quit()
        sys.exit()

    # This part code is hitting yourself
    if new_head in snake:
        print("Game Over! Snake hit itself.")
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += food_weight
        food, food_weight, food_timer = random_food()
    else:
        snake.pop()

    # Food timer: disappears when time runs out
    if time.time() > food_timer:
        food, food_weight, food_timer = random_food()

    # Draw
    for segment in snake:
        screen.blit(snake_img, (segment[0], segment[1]))
    screen.blit(food_img, food)

    # Score and food weight display
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    weight_text = font.render(f"Food:{food_weight}", True, (255,255,255))
    screen.blit(score_text, (10, 10))
    screen.blit(weight_text, (WIDTH-120, 10))

    pygame.display.update()
    clock.tick(10)