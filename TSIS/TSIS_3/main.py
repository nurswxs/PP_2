import pygame, random, sys, os
from persistence import load_data, save_data   # functions for working with JSON (settings, leaderboard)
from ui import UI                             # interface class (menu, text)

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # working directory = file folder

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))     # creating a window
pygame.display.set_caption("Racer Extended")          # window title
clock = pygame.time.Clock()

# uploading settings and leaderboards
settings = load_data("settings.json", {"sound": True, "diff": 1, "user": "Player"})
leaderboard = load_data("leaderboard.json", [])
ui = UI(screen)

IMG_P = "assets/images/"   # the path to the pictures
SND_P = "assets/sounds/"   # The path to sounds

def get_img(name, size):
    # uploads an image and scales it
    return pygame.transform.scale(pygame.image.load(IMG_P + name), size).convert_alpha()

# uploading images
ROAD = pygame.transform.scale(pygame.image.load(IMG_P + "background (2).png"), (WIDTH, HEIGHT))
PLAYER_IMG = get_img("player_car.png", (100, 120))
ENEMY_IMG = get_img("enemy_car.png", (140, 120))
COIN_IMG = get_img("oil.png", (50, 50))
NITRO_IMG = get_img("nitro.png", (50, 50))
SHIELD_IMG = get_img("shield.png", (50, 50))
REPAIR_IMG = get_img("repair.png", (50, 50))

# uploading sounds
try:
    BG_MUSIC = SND_P + "sonican-lo-fi-music-loop-sentimental.mp3"
    CRASH_SND = pygame.mixer.Sound(SND_P + "vau-vau-vau--trombon-neudachi.mp3")
    COIN_SND = pygame.mixer.Sound(SND_P + "button-click-sharp-clear-sonorous.mp3")
except:
    BG_MUSIC = None

def start_game():
    # The main game cycle
    if settings['sound'] and BG_MUSIC and os.path.exists(BG_MUSIC):
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(-1)

    player_rect = PLAYER_IMG.get_rect(center=(WIDTH//2, HEIGHT-70))  # player's position
    
    enemy_rect = None 
    items = []   # list of bonuses
    score, dist, speed = 0, 0, 5 + settings['diff']
    active_pu, pu_timer, has_shield = None, 0, False

    running = True
    while running:
        screen.blit(ROAD, (0, 0))
        dist += speed / 60   # The distance

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.mixer.music.stop()
                return 0 

        # machine control
        keys = pygame.key.get_pressed()
        move = 10 if active_pu == "Nitro" else 6
        if keys[pygame.K_LEFT] and player_rect.left > 0: player_rect.x -= move
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH: player_rect.x += move
        # The screen border is checked so that the car does not go over the edge

        # The appearance of the enemy
        if enemy_rect is None:
            ex = random.choice([75, 155, 245, 325]) 
            enemy_rect = ENEMY_IMG.get_rect(center=(ex, -100))
            # Each frame goes down by a speed of pixels
        enemy_rect.y += speed

        # clash with the enemy
        if player_rect.colliderect(enemy_rect):
            if has_shield:
                has_shield = False; active_pu = None
                enemy_rect = None 
             # If there is a shield, the shield breaks, the enemy disappears, and the game continues.
            else:
                if settings['sound']: pygame.mixer.music.stop(); CRASH_SND.play()
                return int(score + dist)
            # Without a shield, the crash sound plays, and the function returns the final score.

        # The enemy has gone behind the screen
        if enemy_rect and enemy_rect.top > HEIGHT:
            enemy_rect = None
            score += 1
            speed += 0.1 
            # If the enemy has gone beyond the bottom edge,
            # the player gets a point, and the speed increases slightly.

        # the appearance of bonuses
        if random.random() < 0.01:
            itype = random.choice(["Nitro", "Shield", "Repair", "Coin"])
            img = {"Nitro": NITRO_IMG, "Shield": SHIELD_IMG, "Repair": REPAIR_IMG, "Coin": COIN_IMG}[itype]
            items.append({"type": itype, "rect": img.get_rect(center=(random.randint(50, WIDTH-50), -50)), "img": img})

        # bonus processing
        for i in items[:]:
            # a copy of the list to safely delete items during a search.
            i['rect'].y += 5
            if player_rect.colliderect(i['rect']):
                if settings['sound']: COIN_SND.play()
                if i['type'] == "Nitro": active_pu = "Nitro"; pu_timer = 180 # 3 сек
                elif i['type'] == "Shield": active_pu = "Shield"; has_shield = True
                elif i['type'] == "Repair": score += 5
                elif i['type'] == "Coin": score += 2
                items.remove(i)
            elif i['rect'].top > HEIGHT: items.remove(i)

        # bonus timer
        if pu_timer > 0: pu_timer -= 1
        else: active_pu = None if active_pu == "Nitro" else active_pu

        # drawing objects
        screen.blit(PLAYER_IMG, player_rect)
        if enemy_rect: screen.blit(ENEMY_IMG, enemy_rect)
        for i in items: screen.blit(i['img'], i['rect'])
        
        ui.draw_text(f"Score: {score}  Dist: {int(dist)}m", 10, 10, (255,255,255))
        if active_pu: ui.draw_text(f"BUFF: {active_pu}", 10, 40, (255,255,0))
        
        pygame.display.update()
        clock.tick(60)

def main_menu():
    # main menu
    while True:
        ui.show_menu()
        # After the game, the result is added to the high score table.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    res = start_game()
                    if res > 0:
                        leaderboard.append({"name": settings['user'], "score": res})
                        leaderboard.sort(key=lambda x: x['score'], reverse=True)
                        # sort the bill in descending order
                        save_data("leaderboard.json", leaderboard[:10])
                if event.key == pygame.K_2: show_leaderboard()
                if event.key == pygame.K_3: settings_menu()
                if event.key == pygame.K_q: pygame.quit(); sys.exit()

def show_leaderboard():
    # The leaderboard screen
    waiting = True
    while waiting:
        ui.show_leaderboard(leaderboard)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b or event.key == pygame.K_q: waiting = False

def settings_menu():
    # switching the sound in the settings
    settings['sound'] = not settings['sound']
    save_data("settings.json", settings)

if __name__ == "__main__":
    main_menu()   # launching the program