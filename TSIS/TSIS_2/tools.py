import pygame

def flood_fill(surface, x, y, new_color):
    # area fill function (stack fill algorithm)
    target_color = surface.get_at((x,y))        # the original pixel color
    if target_color == new_color: return        # If the color matches, we don't do anything.
    stack = [(x,y)]                             # pixel traversal stack
    while stack:
        px, py = stack.pop()
        if surface.get_at((px,py)) == target_color:
            surface.set_at((px,py), new_color)  # changing the pixel color
            # adding neighboring pixels to the stack
            if px > 0: stack.append((px-1, py))
            if px < surface.get_width()-1: stack.append((px+1, py))
            if py > 0: stack.append((px, py-1))
            if py < surface.get_height()-1: stack.append((px, py+1))

def draw_line(surface, start, end, color, size):
    # draws a line from the start to the end point
    pygame.draw.line(surface, color, start, end, size)

def draw_rect(surface, start, end, color, size):
    # draws a rectangle from the start to the end point
    rect = pygame.Rect(start, (end[0]-start[0], end[1]-start[1]))
    pygame.draw.rect(surface, color, rect, size)

def draw_circle(surface, center, radius, color, size):
    # draws a circle with the center center and radius radius
    pygame.draw.circle(surface, color, center, radius, size)