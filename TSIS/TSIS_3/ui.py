import pygame

class UI:
    def __init__(self, screen):
        # save the screen and create fonts
        self.screen = screen
        self.font = pygame.font.SysFont("Verdana", 20)   # regular font
        self.big_font = pygame.font.SysFont("Verdana", 40) # large font

    def draw_text(self, text, x, y, color=(0,0,0), center=False, big=False):
        # draws text on the screen
        f = self.big_font if big else self.font
        surface = f.render(text, True, color)
        rect = surface.get_rect(center=(x, y)) if center else surface.get_rect(topleft=(x, y))
        self.screen.blit(surface, rect)

    def show_menu(self):
        """Отображает главное меню"""
        self.screen.fill((220, 220, 220)) 
        self.draw_text("RACER PRO", 200, 150, (0, 0, 0), center=True, big=True)
        self.draw_text("1. PLAY GAME", 200, 280, (0, 150, 0), center=True)
        self.draw_text("2. LEADERBOARD", 200, 330, (0, 0, 0), center=True)
        self.draw_text("3. SETTINGS (SOUND)", 200, 380, (0, 0, 0), center=True)
        self.draw_text("Press Q to Quit", 200, 500, (150, 0, 0), center=True)
        pygame.display.update()

    def show_leaderboard(self, data):
        """Отображает таблицу лидеров"""
        self.screen.fill((255, 255, 255))
        self.draw_text("TOP 10 SCORES", 200, 50, (0, 0, 0), center=True, big=True)
        
        if not data:
            # if there is no data
            self.draw_text("No records yet", 200, 250, (100, 100, 100), center=True)
        else:
            # we display the top 10 results
            for i, entry in enumerate(data[:10]):
                text = f"{i+1}. {entry['name']} - {entry['score']}"
                self.draw_text(text, 100, 120 + i*35, (50, 50, 50))
                
        self.draw_text("Press B to go Back", 200, 530, (200, 0, 0), center=True)
        pygame.display.update()