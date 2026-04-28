import pygame, random

CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = 40, 30

class Snake:
    def __init__(self, color):
        # initial parameters of the snake
        self.body = [(10,10)]        # list of segment coordinates
        self.length = 3              # snake length
        self.direction = (1,0)       # direction of movement (X to the right)
        self.color = color           # snake color
        self.shield = False          # the presence of a shield

    def move(self):
        # snake movement
        head = (self.body[0][0]+self.direction[0], self.body[0][1]+self.direction[1])
        self.body.insert(0, head)    # Adding a new head
        if len(self.body) > self.length:
            self.body.pop()          # we remove the tail if the length exceeds

    def eat_food(self, food_type):
        # food processing
        if food_type == "normal":
            self.length += 1
        elif food_type == "poison":
            self.length -= 2
            if self.length <= 1:
                return "gameover"    # loss if length <= 1
        return "ok"

class Food:
    def __init__(self, kind="normal", obstacles=[]):
        # Create food in a random position, avoiding obstacles
        self.kind = kind
        while True:
            pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            if pos not in obstacles:
                self.pos = pos
                break

class Obstacle:
    def __init__(self, level, snake_pos=(10,10)):
        # We create obstacles starting from level 3
        self.blocks = []
        if level >= 3:
            while len(self.blocks) < level*2:
                pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
                # condition: the obstacle must not appear on the snake
                if pos != snake_pos and pos not in self.blocks:
                    self.blocks.append(pos)

class PowerUp:
    TYPES = ["speed","slow","shield"]
    def __init__(self, obstacles=[]):
        # Create a bonus in a random position, avoiding obstacles
        while True:
            pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            if pos not in obstacles:
                self.pos = pos
                break
        self.kind = random.choice(PowerUp.TYPES)   # bonus type
        self.spawn_time = pygame.time.get_ticks()  # Time of appearance
        self.color = {"speed":(0,0,255),"slow":(255,255,0),"shield":(255,0,255)}[self.kind]

    def expired(self):
        # Check: The bonus disappears after 8 seconds
        return pygame.time.get_ticks() - self.spawn_time > 8000