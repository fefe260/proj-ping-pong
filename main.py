import pygame

from model.Bot import Bot
from model.Ball import Ball
from model.Player import Player

from controller.GameManager import GameManager

from constants.window import LARGURA_TELA, ALTURA_TELA

jogador = Player("assets/images/Paddle.png", LARGURA_TELA - 20, ALTURA_TELA / 2, 5)
oponente = Bot("assets/images/Paddle.png", 20, ALTURA_TELA / 2, 5)
grupoPaddle = pygame.sprite.Group()
grupoPaddle.add(jogador)
grupoPaddle.add(oponente)

gameManager = GameManager(jogador, oponente, None, grupoPaddle)

bola = Ball(
    "assets/images/Ball.png",
    LARGURA_TELA / 2,
    ALTURA_TELA / 2,
    4,
    4,
    grupoPaddle,
    gameManager,
)
bolaSprite = pygame.sprite.GroupSingle()
bolaSprite.add(bola)

gameManager.grupoBola = bolaSprite


def main():
    gameManager.gameLoop()


if __name__ == "__main__":
    main()
