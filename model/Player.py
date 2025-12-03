from model.Block import Block
from constants.window import ALTURA_TELA


class Player(Block):
    def __init__(self, path, posX, posY, vel):
        super().__init__(path, posX, posY)
        self.vel = vel
        self.movement = 0

    def tela_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA

    def update(self, grupoBola):
        self.rect.y += self.movement
        self.tela_constrain()
