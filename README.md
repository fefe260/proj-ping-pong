Jogo Ping Pong em Python com Pygame e Multiplayer UDP

Este projeto é uma implementação do clássico jogo Ping Pong, desenvolvida em Python utilizando a biblioteca Pygame.
Inclui modo local contra Bot e modo multiplayer via comunicação em rede utilizando sockets UDP.

O projeto foi desenvolvido praticando conceitos de:
Programação orientada a objetos em Python
Game loop e manipulação de sprites com Pygame
Organização de projeto em camadas (model, controller, assets)
Comunicação em rede com sockets UDP

📄 Descrição do Projeto
O jogo possui dois modos principais:

🎮 1. Modo Local (Single Player)
Você joga contra um Bot que segue a posição da bola automaticamente, simulando um adversário básico.

🌐 2. Modo Multiplayer via UDP
Permite que dois jogadores joguem pela rede local (LAN).
Um jogador executa o servidor
O outro jogador executa o cliente

O servidor é responsável por:
Controlar a posição da bola
Detectar colisões
Atualizar o placar
Sincronizar o estado do jogo entre os jogadores

O jogador apenas:
Envia os comandos de movimento
Desenha na tela o estado recebido do servidor

🛠️ Pré-requisitos

Antes de instalar, certifique-se de ter:

Python 3.8 ou superior
Pip atualizado
Biblioteca Pygame

Para instalar o Pygame:
pip install pygame

📥 Instruções de Instalação
1. Clone este repositório
git clone https://github.com/fefe260/proj-ping-pong.git

2. Acesse a pasta do projeto
cd proj-ping-pong

3. Crie e ative um ambiente virtual (opcional, mas recomendado)
Windows:
python -m venv venv
venv\Scripts\activate

Linux/macOS:
python3 -m venv venv
source venv/bin/activate

4. Instale as dependências
pip install pygame

▶️ Como Executar
🔵 Modo Local (contra Bot)

Na raiz do projeto, execute:

python main.py

🟢 Modo Multiplayer (via UDP)
1. Iniciar o Servidor
cd server
python server.py

2. Iniciar o Cliente

Edite o arquivo:
server/client.py

E altere:
SERVER_IP = "127.0.0.1"

Para o IP do computador que está executando o servidor.

Depois execute:
python client.py


👤 Autoria

Projeto desenvolvido por:

Gustavo
Miguel
Matheus
Fernando
