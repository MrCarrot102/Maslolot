import pygame
from Rzeczy import AnimatedTile

class Wrog(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, '../grafika/wrog/ruch')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = 2.5
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height())

    def ruch(self):
        # Przesuń wroga wzdłuż osi X
        self.rect.x += self.speed
        self.hitbox.x = self.rect.x  # Aktualizuj pozycję hitboxu

    def odwroc_obraz(self):
        # Odwróć obraz wroga w przypadku zmiany kierunku
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def odwroc(self):
        # Odwróć kierunek ruchu wroga
        self.speed *= -1

    def update(self, shift):
        # Zaktualizuj pozycję wroga o wartość przesunięcia
        self.rect.x += shift
        self.hitbox.x += shift  # Aktualizuj pozycję hitboxu
        self.animate()
        self.ruch()
        self.odwroc_obraz()
