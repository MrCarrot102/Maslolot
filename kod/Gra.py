import pygame
import sys
from Okno import *
from Poziomy import Level
from Wybieranie_poziomow import Overworld
from Interfejs import UI

class Game:
    def __init__(self):
        
        # Atrybuty gry
        self.max_level = 2
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0
         
        # Dźwięk
        self.level_bg_music = pygame.mixer.Sound('../dzwieki/muzyka_poziom.mp3')
        self.overworld_bg_music = pygame.mixer.Sound('../dzwieki/muzyka_wybieranie_poziomu.mp3')
        
        # Tworzenie świata gry
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)
        
        # Interfejs użytkownika
        self.ui = UI(screen)
        
        self.paused = False
        self.pause_font = pygame.font.Font(None, 64)
        self.pause_text = self.pause_font.render("PAUZA", True, (255, 255, 255))
        self.pause_text_rect = self.pause_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        self.start_button = pygame.Rect(screen_width // 2 - 75, screen_height // 2 + 50, 150, 50)
        self.start_text = self.pause_font.render("Start", True, (255, 255, 255))
        self.start_text_rect = self.start_text.get_rect(center=self.start_button.center)
        self.quit_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 120, 100, 50)
        self.quit_text = self.pause_font.render("Quit", True, (255, 255, 255))
        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_button.center)

    def create_level(self, current_level):
        
        # Tworzenie poziomu gry
        self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops=-1)

    def create_overworld(self, current_level, new_max_level):
        
        # Tworzenie mapy świata
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)
        self.level_bg_music.stop()

    def change_coins(self, amount):
        
        # Zmiana liczby zebranych monet
        self.coins += amount

    def change_health(self, amount):
       
        # Zmiana aktualnego zdrowia
        self.cur_health += amount

    def check_game_over(self):
       
        # Sprawdzanie, czy gra się zakończyła
        if self.cur_health <= 0:
           
            # Resetowanie stanu gry po przegranej
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
           
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)

    def handle_events(self):
        
        # Obsługa zdarzeń Pygame
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    # Pauza po wciśnięciu klawisza ESC
                    self.paused = not self.paused
                    
                    if self.paused:
                        self.level_bg_music.stop()
                   
                    else:
                        self.level_bg_music.play(loops=-1)
           
            elif event.type == pygame.MOUSEBUTTONDOWN and self.paused:
                
                if self.start_button.collidepoint(event.pos):
                
                    # Powrót do gry po wciśnięciu przycisku "Start"
                    self.paused = False
                    self.level_bg_music.play(loops=-1)
                
                elif self.quit_button.collidepoint(event.pos):
                
                    # Wyjście z gry po wciśnięciu przycisku "Quit"
                    pygame.quit()
                    sys.exit()

    def run(self):
       
        self.handle_events()

        if self.paused:
           
            # Ekran pauzy
            screen.blit(self.pause_text, self.pause_text_rect)
            pygame.draw.rect(screen, (0, 0, 255), self.start_button)
            screen.blit(self.start_text, self.start_text_rect)
            pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
            screen.blit(self.quit_text, self.quit_text_rect)
            return

        if self.status == 'overworld':
            # Uruchamianie trybu do wyboru poziomu
            self.overworld.run()
        
        else:
            
            # Uruchamianie poziomu
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()

# Inicjalizacja Pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()
 
while True:
    
    screen.fill('lightgray')
    game.run()

    pygame.display.update()
    clock.tick(60)
