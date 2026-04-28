import pygame, sys, datetime
from tools import flood_fill, draw_line, draw_rect, draw_circle

pygame.init()
screen = pygame.display.set_mode((800,600)) # this window is 800×600 pixels in size
pygame.display.set_caption("Paint")
canvas = pygame.Surface(screen.get_size()) # a separate surface on which drawing takes place.
canvas.fill((255,255,255))

color = (0,0,0)       # current color
brush_size = 2
tool = "pencil"
drawing = False
start_pos = None
last_pos = None

font = pygame.font.SysFont("Arial", 24)
instruction_font = pygame.font.SysFont("Arial", 18)

text_active = False
text_buffer = ""
text_pos = (0,0)

clock = pygame.time.Clock()

# toolbar
tools_list = ["pencil", "line", "fill", "text"]
button_rects = {}
for i, t in enumerate(tools_list):
    # A rectangle with coordinates and dimensions. 
    # The buttons are positioned horizontally in 100px increments
    button_rects[t] = pygame.Rect(10 + i*100, 10, 90, 30)

# color panel
colors = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,165,0)]
color_buttons = {}
for i, c in enumerate(colors):
    # Creates color buttons
    color_buttons[c] = pygame.Rect(10 + i*40, 50, 30, 30)

def draw_panel():
    # toolbar
    for t in tools_list:
        rect = button_rects[t]
        pygame.draw.rect(screen, (200,200,200), rect)
        label = font.render(t, True, (0,0,0))
        screen.blit(label, (rect.x+10, rect.y+5))
        if tool == t:
            pygame.draw.rect(screen, (0,0,255), rect, 2)
    # color panel
    for c, rect in color_buttons.items():
        pygame.draw.rect(screen, c, rect)
        if color == c:
            pygame.draw.rect(screen, (0,0,0), rect, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # tool selection
            for t, rect in button_rects.items():
                if rect.collidepoint(event.pos):
                    # collidepoint — checks whether the click point has hit the rectangle of the button.
                    tool = t
                    text_active = False
                    print("Tool selected:", tool)
            # color selection
            for c, rect in color_buttons.items():
                if rect.collidepoint(event.pos):
                    color = c
                    print("Color selected:", color)

            # tool actions
            if tool == "pencil":
                drawing = True
                last_pos = event.pos # memorizing the starting point
            elif tool == "line":
                drawing = True
                start_pos = event.pos # memorizing the beginning of the line
            elif tool == "fill": # fill it up immediately
                flood_fill(canvas, event.pos[0], event.pos[1], color)
            elif tool == "text":
                text_pos = event.pos # memorizing the place for the text
                text_active = True
                text_buffer = "" # clearing the buffer

        elif event.type == pygame.MOUSEBUTTONUP:
            if tool == "pencil":
                drawing = False # stop drawing
            elif tool == "line" and drawing:
                draw_line(canvas, start_pos, event.pos, color, brush_size)
                drawing = False # draw a line from the start to the end point

        elif event.type == pygame.MOUSEMOTION:
            if tool == "pencil" and drawing:
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: brush_size = 2
            elif event.key == pygame.K_2: brush_size = 5
            elif event.key == pygame.K_3: brush_size = 10

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                # The file name contains the date and time so as not to overwrite the previous ones.
                filename = f"canvas_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            if text_active:
                if event.key == pygame.K_RETURN:
                    # turns a line into a picture
                    text_surface = font.render(text_buffer, True, color)
                    canvas.blit(text_surface, text_pos)
                    text_active = False
                elif event.key == pygame.K_ESCAPE:
                    # Just cancels the input
                    text_active = False
                elif event.key == pygame.K_BACKSPACE:
                    # delete the last character
                    text_buffer = text_buffer[:-1]
                elif event.key == pygame.K_DELETE:
                    pygame.draw.rect(canvas, (255,255,255), (text_pos[0], text_pos[1], 200, 30))
                    # erases any old text in that area.
                    text_buffer = ""
                elif event.key == pygame.K_t and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    with open("text_log.txt", "a", encoding="utf-8") as f:
                        f.write(f"{text_buffer}\n")
                    print("Text saved:", text_buffer)
                else:
                    text_buffer += event.unicode

    screen.blit(canvas, (0,0))
    if text_active:
        preview = font.render(text_buffer, True, color)
        screen.blit(preview, text_pos)

    draw_panel()

    instructions = "Text tool: Enter - бекіту, Esc - болдырмау, Backspace - өшіру, Delete - тазалау, Ctrl+T - мәтінді сақтау"
    instr_surface = instruction_font.render(instructions, True, (0,0,0))
    screen.blit(instr_surface, (10, screen.get_height()-30))

    pygame.display.flip()
    clock.tick(60)