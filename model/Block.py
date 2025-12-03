import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, path, posX, posY):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(posX, posY))
