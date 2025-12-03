import pygame
import sys

from constants.window import (
    LARGURA_TELA,
    ALTURA_TELA,
    BACKGROUND_COLOR,
    LINHA_CENTRAL,
    FONT_JOGO,
)


class GameManager:
    def __init__(self, jogador, oponente, grupoBola, grupoPaddle):
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.scoreJogador = 0
        self.scoreOponente = 0
        self.jogador = jogador
        self.oponente = oponente
        self.grupoBola = grupoBola
        self.grupoPaddle = grupoPaddle

    def runGame(self):
        pygame.display.set_caption("UDPong")

        self.grupoPaddle.draw(self.tela)
        self.grupoBola.draw(self.tela)

        self.grupoPaddle.update(self.grupoBola)
        self.grupoBola.update()
        self.resetBola()
        self.desenhaScore()

    def resetBola(self):
        if self.grupoBola.sprite.rect.right >= LARGURA_TELA:
            self.scoreOponente += 1
            self.grupoBola.sprite.resetBola()
        if self.grupoBola.sprite.rect.left <= 0:
            self.scoreJogador += 1
            self.grupoBola.sprite.resetBola()

    def desenhaScore(self):
        scoreJogador = FONT_JOGO.render(
            str(self.scoreJogador), True, pygame.Color("White")
        )
        scoreOponente = FONT_JOGO.render(
            str(self.scoreOponente), True, pygame.Color("White")
        )

        scoreJogadorRect = scoreJogador.get_rect(
            midleft=(LARGURA_TELA / 2 + 40, ALTURA_TELA / 2)
        )
        scoreOponenteRect = scoreOponente.get_rect(
            midleft=(LARGURA_TELA / 2 - 40, ALTURA_TELA / 2)
        )

        self.tela.blit(scoreJogador, scoreJogadorRect)
        self.tela.blit(scoreOponente, scoreOponenteRect)

    def gameLoop(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.jogador.movement -= self.jogador.vel
                    if event.key == pygame.K_DOWN:
                        self.jogador.movement += self.jogador.vel

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.jogador.movement -= self.jogador.vel
                    if event.key == pygame.K_UP:
                        self.jogador.movement += self.jogador.vel

            self.tela.fill(BACKGROUND_COLOR)
            pygame.draw.rect(self.tela, pygame.Color("white"), LINHA_CENTRAL)

            self.runGame()

            pygame.display.flip()
            clock.tick(120)
