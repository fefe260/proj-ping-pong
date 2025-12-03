import socket
import json
import time
import pygame
import random

from model.Player import Player
from model.Ball import Ball
from constants.window import LARGURA_TELA, ALTURA_TELA

pygame.init()

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))
sock.setblocking(False)

print("Servidor iniciado em", SERVER_PORT)

# --- ENTIDADES DO JOGO (rodam no servidor) ---
p1 = Player("assets/images/Paddle.png", LARGURA_TELA - 20, ALTURA_TELA // 2, 5)
p2 = Player("assets/images/Paddle.png", 20, ALTURA_TELA // 2, 5)
p2.movement = 0

grupoPaddle = pygame.sprite.Group(p1, p2)

ball_group = pygame.sprite.GroupSingle()
ball_group.add(
    Ball(
        "assets/images/Ball.png",
        LARGURA_TELA // 2,
        ALTURA_TELA // 2,
        4,
        4,
        grupoPaddle,
        None,
    )
)

ball = ball_group.sprite

score1 = 0
score2 = 0

clients = []  # até 2 jogadores
inputs = {}


def handle_inputs():
    """Recebe os inputs dos clientes."""
    global inputs, clients
    try:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()

        if addr not in clients and len(clients) < 2:
            clients.append(addr)
            print("Novo jogador:", addr)

        if msg.startswith("input:"):
            comando = msg.split(":")[1]
            inputs[addr] = comando

    except:
        pass


def apply_inputs():
    """Aplica o movimento recebido dos clientes."""
    if len(clients) >= 1:
        cmd = inputs.get(clients[0], "")
        if cmd == "UP":
            p1.movement = -p1.vel
        elif cmd == "DOWN":
            p1.movement = p1.vel
        else:
            p1.movement = 0

    if len(clients) >= 2:
        cmd = inputs.get(clients[1], "")
        if cmd == "UP":
            p2.movement = -p2.vel
        elif cmd == "DOWN":
            p2.movement = p2.vel
        else:
            p2.movement = 0


def send_state():
    """Envia estado completo a todos os clientes."""
    state = {
        "ball": [ball.rect.x, ball.rect.y],
        "p1": p1.rect.y,
        "p2": p2.rect.y,
        "score1": score1,
        "score2": score2,
    }
    packet = json.dumps(state).encode()

    for c in clients:
        sock.sendto(packet, c)


clock = pygame.time.Clock()

print("Servidor rodando...")

while True:
    handle_inputs()
    apply_inputs()

    # atualizar paddles
    grupoPaddle.update(ball_group)

    # atualizar bola
    ball.update()

    # pontuação
    if ball.rect.right >= LARGURA_TELA:
        score2 += 1
        ball.resetBola()
    if ball.rect.left <= 0:
        score1 += 1
        ball.resetBola()

    send_state()

    clock.tick(120)
