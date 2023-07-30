import pygame 
from Okno import *
from csv import reader 
from os import walk 

def import_folder(path):
    surface_list = []

    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


def import_csv_layout(path):
    terrain_map = []
    with open(path) as map_file:
        level = reader(map_file, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
    return terrain_map


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surf)

    return cut_tiles


"""
Funkcja import_folder importuje wszystkie pliki graficzne z podanego folderu 
jako powierzchnie (surfaces). 
Funkcja przechodzi przez wszystkie pliki w folderze i używa pygame.image.load do załadowania 
ich jako powierzchnie Surface. Następnie dodaje te powierzchnie do listy surface_list, którą zwraca na koniec.
Funkcja import_csv_layout importuje układ poziomu z pliku CSV. 
Otwiera plik CSV za pomocą open i korzysta z csv.reader do odczytania zawartości. 
Każdy wiersz zapisuje jako listę i dodaje go do listy terrain_map, którą zwraca na koniec.
Funkcja import_cut_graphics importuje grafiki podzielone na kafelki z 
jednego obrazu. Ładuje obraz za pomocą pygame.image.load i następnie
oblicza liczbę kafelków wzdłuż osi x i y na podstawie rozmiaru obrazu i 
rozmiaru kafelka. Następnie przechodzi przez wszystkie kafelki, tworząc nową 
powierzchnię Surface dla każdego kafelka za pomocą pygame.Surface. Kopiuje odpowiedni 
fragment obrazu do nowej powierzchni i dodaje ją do listy cut_tiles, którą zwraca na koniec.
"""