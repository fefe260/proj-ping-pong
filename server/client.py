import pygame
import socket
import json
import sys

from constants.window import *
from model.Player import Player
from model.Ball import Ball

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)

pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("UDPong Cliente")

clock = pygame.time.Clock()

# objetos locais apenas para DESENHAR
p1 = Player("assets/images/Paddle.png", LARGURA_TELA - 20, ALTURA_TELA / 2, 0)
p2 = Player("assets/images/Paddle.png", 20, ALTURA_TELA / 2, 0)
ball = Ball(
    "assets/images/Ball.png", LARGURA_TELA / 2, ALTURA_TELA / 2, 0, 0, None, None
)


def send(command):
    sock.sendto(f"input:{command}".encode(), (SERVER_IP, SERVER_PORT))

score1 = 0
score2 = 0

while True:
    # INPUT local -> servidor
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        send("UP")
    elif keys[pygame.K_DOWN]:
        send("DOWN")
    else:
        send("NONE")

    # RECEBER ESTADO DO SERVIDOR
    try:
        data, _ = sock.recvfrom(1024)
        state = json.loads(data.decode())

        ball.rect.x, ball.rect.y = state["ball"]
        p1.rect.y = state["p1"]
        p2.rect.y = state["p2"]
        score1 = state["score1"]
        score2 = state["score2"]

    except:
        pass

    # DESENHAR
    tela.fill(BACKGROUND_COLOR)
    pygame.draw.rect(tela, pygame.Color("white"), LINHA_CENTRAL)

    tela.blit(p1.image, p1.rect)
    tela.blit(p2.image, p2.rect)
    tela.blit(ball.image, ball.rect)

    s1 = FONT_JOGO.render(str(score1), True, pygame.Color("white"))
    s2 = FONT_JOGO.render(str(score2), True, pygame.Color("white"))

    tela.blit(s1, s1.get_rect(midleft=(LARGURA_TELA / 2 + 40, ALTURA_TELA / 2)))
    tela.blit(s2, s2.get_rect(midleft=(LARGURA_TELA / 2 - 40, ALTURA_TELA / 2)))

    pygame.display.flip()
    clock.tick(120)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
