import pygame
from Grafika import import_folder

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5

        if type == 'skok':
            self.frames = import_folder('../grafika/postac/drobinki/skok')
        elif type == 'londowanie':
            self.frames = import_folder('../grafika/postac/drobinki/londowanie')
        elif type == 'wybuch':
            self.frames = import_folder('../grafika/wrog/wybuch')

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed

        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift

# Klasa ParticleEffect reprezentuje efekt cząsteczkowy w grze. 
# Inicjalizuje się podając pozycję efektu oraz typ. Na podstawie typu wybierane są 
# odpowiednie klatki animacji za pomocą funkcji import_folder z modułu support.
# Metoda animate odpowiada za odtwarzanie animacji cząsteczkowej. 
# Zwiększa indeks klatki animacji o wartość animation_speed, 
# a następnie aktualizuje obrazek cząsteczki. 
# Jeśli indeks przekroczy ilość dostępnych klatek, 
# cząsteczka zostaje usunięta.
# Metoda update odpowiada za aktualizację pozycji cząsteczki na ekranie. 
# Dodaje przesunięcie x_shift do aktualnej pozycji cząsteczki, 
# co umożliwia jej przesuwanie się wraz z innymi elementami gry.