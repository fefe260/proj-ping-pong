import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

LARGURA_TELA = 700
ALTURA_TELA = 400

BACKGROUND_COLOR = pygame.Color("#2F373F")
LINHA_CENTRAL = pygame.Rect(LARGURA_TELA / 2 - 2, 0, 4, ALTURA_TELA)
FONT_JOGO = pygame.font.Font("freesansbold.ttf", 30)
