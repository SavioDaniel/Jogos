Jogo da Velha com IA
Este é um projeto de Jogo da Velha desenvolvido em Python usando a biblioteca Pygame. O jogo inclui uma inteligência artificial baseada no algoritmo Minimax, permitindo que o jogador humano jogue contra a máquina.

📋 Funcionalidades
Tabuleiro interativo com interface gráfica.
Placar que registra as vitórias do jogador e da IA.
Botões para Reiniciar o jogo ou Sair.
Alternância automática entre o jogador humano e a IA.
Algoritmo Minimax para jogadas estratégicas da IA.
O jogador humano sempre joga como "X", e a IA joga como "O".
🛠️ Tecnologias utilizadas
Python
Pygame

🎮 Como jogar
Faça o download ou clone este repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/jogo-da-velha-com-ia.git
cd jogo-da-velha-com-ia
Certifique-se de que o Python e o Pygame estão instalados:
bash
Copiar código
pip install pygame
Execute o jogo:
bash
Copiar código
python main.py
Clique em uma célula vazia para fazer sua jogada. A IA fará sua jogada automaticamente. O jogo termina quando há um vencedor ou o tabuleiro está cheio.

📂 Estrutura do projeto
bash
Copiar código
jogo-da-velha-com-ia/
│
├── main.py        # Código principal do jogo
├── README.md      # Documentação do projeto
└── requirements.txt # Lista de dependências

🧠 Como funciona a IA?
A inteligência artificial utiliza o algoritmo Minimax para calcular a jogada ótima. Este algoritmo explora todas as possibilidades de jogadas futuras, atribuindo pontuações com base nos cenários possíveis:

+1 para vitórias da IA.
-1 para vitórias do jogador.
0 para empates.
A IA escolhe sempre a jogada que maximiza sua chance de vencer.

📝 Melhorias possíveis
Adicionar diferentes níveis de dificuldade para a IA.
Melhorar o design da interface gráfica.
Suporte para jogos multiplayer local.
