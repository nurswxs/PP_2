import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame, sys, json, random
from db import save_result, top10, personal_best   # working with the database
from game import Snake, Food, Obstacle, PowerUp, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT  # game classes

pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH*CELL_SIZE, GRID_HEIGHT*CELL_SIZE))  # creating a window
pygame.display.set_caption("Snake Game")

# downloading settings from JSON
with open("settings.json") as f: settings = json.load(f)



pygame.mixer.init()
# uploading sounds
eat_sound = pygame.mixer.Sound("assets/sounds/free-sound-1674743464.mp3")
gameover_sound = pygame.mixer.Sound("assets/sounds/free-sound-1675012530.mp3")
pygame.mixer.music.load("assets/sounds/super-mario-bros_2.mp3")

# setting the volume
eat_sound.set_volume(1.0 if settings["sound"] else 0.0)
gameover_sound.set_volume(1.0 if settings["sound"] else 0.0)
pygame.mixer.music.set_volume(1.0 if settings["sound"] else 0.0)

if settings["sound"]:
    pygame.mixer.music.play(-1)   # background music

def load_scaled(path):
    # loads the image and scales it to fit the cell size
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))

# uploading images
background_img = pygame.image.load("assets/images/background (3).png")
snake_img = load_scaled("assets/images/snake (1).png")
food_img = load_scaled("assets/images/food (1).png")
poison_img = load_scaled("assets/images/poison.png")

username = ""   # player's name


# The screen for entering the player's name before launching. 
# It works the same way as the text tool in Paint from the previous code.
def username_entry():
    # entering the user name
    global username
    font = pygame.font.SysFont("Arial", 36)
    input_box = pygame.Rect(250, 250, 300, 50)
    active = True
    text = ""
    while active:
        screen.blit(background_img, (0,0))
        txt_surface = font.render("Enter Username: " + text, True, (255,255,255))
        screen.blit(txt_surface, (250,200))
        pygame.draw.rect(screen, (255,255,255), input_box, 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username = text
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

def main_menu():
    # main menu
    # A simple menu on the keys. Each frame draws the background and buttons,
    # and waits for them to be clicked.
    running = True
    font = pygame.font.SysFont("Arial", 36)
    while running:
        screen.blit(background_img, (0,0))
        play_text = font.render("Play (P)", True, (255,255,255))
        score_text = font.render("Leaderboard (L)", True, (255,255,255))
        settings_text = font.render("Settings (S)", True, (255,255,255))
        quit_text = font.render("Quit (Q)", True, (255,255,255))
        screen.blit(play_text, (300,160))
        screen.blit(score_text, (270,260))
        screen.blit(settings_text, (280,360))
        screen.blit(quit_text, (320,460))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: run_game(username)
                elif event.key == pygame.K_l: leaderboard_screen()
                elif event.key == pygame.K_s: settings_screen()
                elif event.key == pygame.K_q: pygame.quit(); sys.exit()

def leaderboard_screen():
    # The leaderboard screen
    rows = top10() # top10() returns a list from the database
    font = pygame.font.SysFont("Arial", 24)
    running = True
    while running:
        screen.fill((0,0,0))
        y = 50
        for i,row in enumerate(rows): # enumerate gives the row number (1, 2, 3...)
            # of each row: place, name, points, level, date
            text = font.render(f"{i+1}. {row[0]} {row[1]} pts Level {row[2]} {row[3]}", True, (255,255,255))
            screen.blit(text, (20,y)); y+=30
        back_text = font.render("Press ESC to return", True, (255,255,255))
        screen.blit(back_text, (20, y+40))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

def settings_screen():
    # Settings screen (sound ON/OFF)
    running = True
    font = pygame.font.SysFont("Arial", 24)
    while running: 
        # Immediately saves it to settings.json and applies it to sounds.
        screen.fill((0,0,0))
        text = font.render(f"Sound: {'ON' if settings['sound'] else 'OFF'}", True, (255,255,255))
        screen.blit(text, (250,250))
        back_text = font.render("Press ESC to return", True, (255,255,255))
        screen.blit(back_text, (250,300))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # audio switching
                    settings["sound"] = not settings["sound"]
                    with open("settings.json","w") as f: json.dump(settings,f)
                    if settings["sound"]:
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(1.0)
                        eat_sound.set_volume(1.0)
                        gameover_sound.set_volume(1.0)
                    else:
                        pygame.mixer.music.stop()
                        eat_sound.set_volume(0.0)
                        gameover_sound.set_volume(0.0)
                elif event.key == pygame.K_ESCAPE:
                    running = False

def game_over_screen(username, score, level):
    # Game Over Screen
    best = personal_best(username)
    save_result(username, score, level)
    running = True
    font = pygame.font.SysFont("Arial", 36)
    # First, he gets a personal best before saving it to show the old best result.
    # Then saves the new result to the database.
    while running:
        screen.blit(background_img, (0,0))
        if settings["sound"]: gameover_sound.play()
        text = font.render(f"Game Over! Score: {score} Best: {best}", True, (255,255,255))
        screen.blit(text, (100, 200))
        back_text = font.render("Press ESC to return", True, (255,255,255))
        screen.blit(back_text, (100, 260))
        pygame.display.flip()
        # Shows Game Over, score and high score
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

def run_game(username):
    # The main game cycle
    snake = Snake(tuple(settings["snake_color"]))
    food = Food("normal")
    poison = Food("poison")
    obstacles = Obstacle(1)
    powerup = None
    clock = pygame.time.Clock()
    score, level = 0, 1
    speed = 10
    running = True
    powerup_start = None

    while running:
        # event handling
        for event in pygame.event.get():
            # The direction is given as a vector (x, y). For example (1,0) = right.
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: snake.direction=(0,-1)
                elif event.key == pygame.K_DOWN: snake.direction=(0,1)
                elif event.key == pygame.K_LEFT: snake.direction=(-1,0)
                elif event.key == pygame.K_RIGHT: snake.direction=(1,0)

        snake.move()

        # food inspection
        # snake.body[0] — the snake's head. If it matches the position of the food, we eat it.
        if snake.body[0] == food.pos:
            snake.eat_food("normal")
            score += 10
            if settings["sound"]: eat_sound.play()
            food = Food("normal", obstacles.blocks)

        # Checking the poison
        if snake.body[0] == poison.pos:
            if snake.eat_food("poison") == "gameover":
                game_over_screen(username, score, level)
                return
            # The poison can kill the snake — if eat_food returns "gameover", the game ends.
            if settings["sound"]: gameover_sound.play()
            poison = Food("poison", obstacles.blocks)

        # the appearance of bonuses
        if powerup is None and random.randint(0,200) == 1:
            powerup = PowerUp(obstacles.blocks)
        if powerup and powerup.expired():
            powerup = None

        if powerup and snake.body[0] == powerup.pos:
            # bonus activation
            if powerup.kind == "speed":
                speed = 20; powerup_start = pygame.time.get_ticks()
            elif powerup.kind == "slow":
                speed = 5; powerup_start = pygame.time.get_ticks()
            elif powerup.kind == "shield":
                snake.shield = True
            powerup = None

        # collision checking
        head_x, head_y = snake.body[0]
        if (head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT
            or snake.body[0] in snake.body[1:]
            or snake.body[0] in obstacles.blocks):
            if snake.shield:
                snake.shield = False   # The shield saves once
            else:
                game_over_screen(username, score, level)
                return

        # Level up every 50 points
        # Every 50 points — a new level with more obstacles
        if score // 50 + 1 > level:
            level += 1
            obstacles = Obstacle(level, snake.body[0])

        # drawing objects
        screen.blit(background_img, (0,0))
        screen.blit(food_img, (food.pos[0]*CELL_SIZE, food.pos[1]*CELL_SIZE))
        screen.blit(poison_img, (poison.pos[0]*CELL_SIZE, poison.pos[1]*CELL_SIZE))
        if powerup:
            pygame.draw.rect(screen, powerup.color,
                             (powerup.pos[0]*CELL_SIZE, powerup.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for ox, oy in obstacles.blocks:
            pygame.draw.rect(screen, (150,150,150), (ox*CELL_SIZE, oy*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for x,y in snake.body:
            screen.blit(snake_img, (x*CELL_SIZE, y*CELL_SIZE))

        # text output (points, level, player)
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}  Level: {level}", True, (255,255,255))
        screen.blit(score_text, (10,10))
        user_text = font.render(f"Player: {username}", True, (255,255,255))
        screen.blit(user_text, (10,40))

        pygame.display.flip()

        # speed refund after bonus
        if powerup_start and pygame.time.get_ticks() - powerup_start > 5000:
            speed = 10 + level
            powerup_start = None

        clock.tick(speed)

if __name__ == "__main__":
    username_entry()   # entering the player's name
    main_menu()        # launching the main menu