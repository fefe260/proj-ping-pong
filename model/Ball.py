import pygame
import random

from model.Block import Block

from constants.sound_effects import SOM_PONG, SOM_SCORE
from constants.window import ALTURA_TELA, LARGURA_TELA, FONT_JOGO, BACKGROUND_COLOR


class Ball(Block):
    def __init__(self, path, posX, posY, velX, velY, paddles, gameManager):
        super().__init__(path, posX, posY)
        self.velX = velX * random.choice((-1, 1))
        self.velY = velY * random.choice((-1, 1))
        self.paddles = paddles
        self.active = False
        self.scoreTempo = 0
        self.gameManager = gameManager

    def update(self):
        if self.active:
            self.rect.x += self.velX
            self.rect.y += self.velY
            self.collisions()
        else:
            # self.restartCounter(self.gameManager.tela)
            if self.gameManager is not None:
                self.restartCounter(self.gameManager.tela)
            else:
                tempoAtual = pygame.time.get_ticks()
                if tempoAtual - self.scoreTempo >= 2100:
                    self.active = True
        

    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            pygame.mixer.Sound.play(SOM_PONG)
            self.velY *= -1

        if pygame.sprite.spritecollide(self, self.paddles, False):
            pygame.mixer.Sound.play(SOM_PONG)
            collisionPaddle = pygame.sprite.spritecollide(self, self.paddles, False)[
                0
            ].rect
            if abs(self.rect.right - collisionPaddle.left) < 10 and self.velX > 0:
                self.velX *= -1
            if abs(self.rect.left - collisionPaddle.right) < 10 and self.velX < 0:
                self.velX *= -1
            if abs(self.rect.top - collisionPaddle.bottom) < 10 and self.velY < 0:
                self.rect.top = collisionPaddle.bottom
                self.velY *= -1
            if abs(self.rect.bottom - collisionPaddle.top) < 10 and self.velY > 0:
                self.rect.bottom = collisionPaddle.top
                self.velY *= -1

    def resetBola(self):
        self.active = False
        self.velX *= random.choice((-1, 1))
        self.velY *= random.choice((-1, 1))
        self.scoreTempo = pygame.time.get_ticks()
        self.rect.center = (LARGURA_TELA / 2, ALTURA_TELA / 2)
        pygame.mixer.Sound.play(SOM_SCORE)

    def restartCounter(self, tela):
        tempoAtual = pygame.time.get_ticks()
        numCountdowm = 3

        if tempoAtual - self.scoreTempo <= 700:
            numCountdowm = 3
        if 700 < tempoAtual - self.scoreTempo <= 1400:
            numCountdowm = 2
        if 1400 < tempoAtual - self.scoreTempo <= 2100:
            numCountdowm = 1
        if tempoAtual - self.scoreTempo >= 2100:
            self.active = True

        contTempo = FONT_JOGO.render(str(numCountdowm), True, pygame.Color("white"))
        contTempoRect = contTempo.get_rect(
            center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + 50)
        )

        pygame.draw.rect(tela, BACKGROUND_COLOR, contTempoRect)
        tela.blit(contTempo, contTempoRect)
