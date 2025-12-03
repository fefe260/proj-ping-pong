from model.Block import Block
from constants.window import ALTURA_TELA


class Bot(Block):
    def __init__(self, path, posX, posY, vel):
        super().__init__(path, posX, posY)
        self.vel = vel

    def tela_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA

    def update(self, grupoBola):
        if self.rect.top < grupoBola.sprite.rect.y:
            self.rect.y += self.vel
        if self.rect.bottom > grupoBola.sprite.rect.y:
            self.rect.y -= self.vel
        self.tela_constrain()
