é uma implementação do clássico jogo Ping Pong, desenvolvida em Python utilizando a biblioteca Pygame.
O projeto inclui modo local contra Bot e modo multiplayer usando comunicação em rede via sockets UDP.

Ele foi desenvolvido para fins educacionais, praticando conceitos de:

Programação orientada a objetos em Python

Game loop e manipulação de sprites com Pygame

Organização de projeto em camadas (model, controller, assets)

📄 Descrição do Projeto

O jogo possui dois modos principais:

🎮 1. Modo Local (Single Player)

Você joga contra um Bot que segue a posição da bola.

🌐 2. Modo Multiplayer via UDP

Um jogador roda o servidor, enquanto outros rodam o cliente, permitindo jogar Pong pela rede local (LAN) usando pacotes UDP.

O servidor controla:

posição da bola

colisões

placar

sincronização dos jogadores

Os clientes apenas enviam movimentos e desenham o estado recebido.

🛠️ Pré-requisitos

Antes de instalar, certifique-se de ter:

Python 3.8 ou superior

Pip atualizado

Biblioteca Pygame

Para instalar o pygame:

pip install pygame

📥 Instruções de Instalação

Clone este repositório:

git clone https://github.com/fefe260/UDPong.git


Acesse a pasta do projeto:

cd UDPong


 Crie e ative um ambiente virtual:

python -m venv venv


Windows:

venv\Scripts\activate


Linux/macOS:

source venv/bin/activate


Instale as dependências:

pip install pygame

▶️ Como Executar
🔵 Modo Local 

Na raiz do projeto:

python main.py

🟢 Modo Multiplayer (via UDP)
1. Iniciar o Servidor
cd server
python server.py

2. Iniciar o Cliente

Edite o arquivo server/client.py
Altere SERVER_IP = "127.0.0.1" para o IP da máquina que roda o servidor.

Execute:

python client.py


📂 Estrutura do Projeto
UDPong/
│── assets/
│   ├── images/ (sprites)
│   └── sounds/ (efeitos sonoros)
│── model/ (Player, Bot, Ball, etc.)
│── controller/ (GameManager)
│── constants/ (tamanho de tela, sons)
│── server/ (server.py e client.py)
│── main.py
│── README.md

👤 Autoria

Projeto desenvolvido por Gustavo,Miguel,Matheus, e Fernando como atividade prática para estudos de:

Programação em Python

Jogos com Pygame

Comunicação em rede com sockets UDP