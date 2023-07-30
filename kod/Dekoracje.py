import pygame
from Grafika import import_folder
from random import choice, randint
from Okno import vertical_tile_number, tile_size, screen_width
from Rzeczy import AnimatedTile, StaticTile


class Sky:
    def __init__(self, horizon, style='level'):
        self.sky_surface = pygame.image.load('../grafika/dekoracje/niebo/niebo.png').convert()
        self.horizon = horizon

        # Rozciągnij obraz na całą szerokość ekranu
        self.sky_surface = pygame.transform.scale(self.sky_surface, (screen_width, tile_size * vertical_tile_number))

        self.style = style

    def draw(self, surface):
        # Rysuj powierzchnię nieba na ekranie
        surface.blit(self.sky_surface, (0, 0))


class Water:
    def __init__(self, top, level_width):
        water_start = -screen_width
        water_tile_width = 192
        tile_x_amount = int((level_width + screen_width * 2) / water_tile_width)
        self.water_sprites = pygame.sprite.Group()

        # Dodaj animowane kafelki wody
        for tile in range(tile_x_amount):
            x = tile * water_tile_width + water_start
            y = top
            sprite = AnimatedTile(192, x, y, '../grafika/dekoracje/woda')
            self.water_sprites.add(sprite)

    def draw(self, surface, shift):
        # Zaktualizuj i narysuj animowane kafelki wody
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)
