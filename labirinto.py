import pygame
import heapq
import numpy as np
import time

TAMANHO_BLOCO = 40
LINHAS = 10
COLUNAS = 15
LARGURA_TELA = COLUNAS * TAMANHO_BLOCO
ALTURA_TELA = LINHAS * TAMANHO_BLOCO
CORES = {
    "parede": (0, 0, 0),
    "caminho": (255, 255, 255),
    "inicio": (0, 255, 0),
    "fim": (255, 0, 0),
    "visitado": (100, 100, 255),
    "caminho_final": (255, 255, 0)
}

def a_star(labirinto, inicio, fim):
    def heuristica(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    fila = []
    heapq.heappush(fila, (0, inicio))
    custo = {inicio: 0}
    caminhos = {inicio: None}

    visitados = []

    while fila:
        _, atual = heapq.heappop(fila)
        visitados.append(atual)

        if atual == fim:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = caminhos[atual]
            return caminho[::-1], visitados

        x, y = atual
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vizinho = (x + dx, y + dy)
            if 0 <= vizinho[0] < len(labirinto) and 0 <= vizinho[1] < len(labirinto[0]) and labirinto[vizinho[0]][vizinho[1]] == 0:
                novo_custo = custo[atual] + 1
                if vizinho not in custo or novo_custo < custo[vizinho]:
                    custo[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, fim)
                    heapq.heappush(fila, (prioridade, vizinho))
                    caminhos[vizinho] = atual
    return None, visitados

labirinto = np.random.choice([0, 1], size=(LINHAS, COLUNAS), p=[0.7, 0.3])  
labirinto[0][0] = 0  
labirinto[LINHAS-1][COLUNAS-1] = 0  

def desenha_labirinto(tela, labirinto, inicio, fim, visitados=[], caminho=[]):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            cor = CORES["parede"] if labirinto[i][j] == 1 else CORES["caminho"]
            pygame.draw.rect(tela, cor, (j * TAMANHO_BLOCO, i * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))
            pygame.draw.rect(tela, (200, 200, 200), (j * TAMANHO_BLOCO, i * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 1)
    for v in visitados:
        pygame.draw.rect(tela, CORES["visitado"], (v[1] * TAMANHO_BLOCO, v[0] * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))
    for p in caminho:
        pygame.draw.rect(tela, CORES["caminho_final"], (p[1] * TAMANHO_BLOCO, p[0] * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))
    pygame.draw.rect(tela, CORES["inicio"], (inicio[1] * TAMANHO_BLOCO, inicio[0] * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))
    pygame.draw.rect(tela, CORES["fim"], (fim[1] * TAMANHO_BLOCO, fim[0] * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Labirinto - Algoritmo A* com Animação")

inicio = (0, 0)
fim = (LINHAS - 1, COLUNAS - 1)

rodando = True
caminho = []
visitados = []
posicao_atual = inicio
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = y // TAMANHO_BLOCO, x // TAMANHO_BLOCO
            if evento.button == 1:  
                inicio = (grid_x, grid_y)
                posicao_atual = inicio
            elif evento.button == 3:  
                fim = (grid_x, grid_y)

            if labirinto[grid_x][grid_y] == 1:
                continue  

            caminho, visitados = a_star(labirinto, inicio, fim)

    if caminho and posicao_atual != fim:
        proxima_posicao = caminho.pop(0)
        posicao_atual = proxima_posicao
        time.sleep(0.2)  

    tela.fill((0, 0, 0))
    desenha_labirinto(tela, labirinto, posicao_atual, fim, visitados, caminho)
    pygame.display.flip()

pygame.quit()
