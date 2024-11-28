import heapq
from collections import deque

def reconstruir_caminho(caminhos, start, goal):
    caminho = []
    atual = goal
    while atual is not None:
        caminho.append(atual)
        atual = caminhos[atual]
    return caminho[::-1]

def busca_largura(labirinto, start, goal):
    fila = deque([start])
    visitados = set([start])  # Conjunto de vértices visitados
    caminhos = {start: None}  # Reconstrução do caminho
    ordem_visita = []  # Registrar a ordem de visita

    while fila:
        atual = fila.popleft()
        ordem_visita.append(atual)  # Registra a ordem de visitação

        for vizinho in labirinto.vizinhos_validos(*atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                caminhos[vizinho] = atual
                fila.append(vizinho)

    return reconstruir_caminho(caminhos, start, goal), visitados, ordem_visita

def busca_profundidade(labirinto, start, goal):
    pilha = [start]
    visitados = set()
    caminhos = {start: None}
    ordem_visita = []
    ordem_atual = 1
    ordem_map = {}

    while pilha:
        atual = pilha.pop()

        if atual not in visitados:
            visitados.add(atual)
            ordem_visita.append(atual)
            ordem_map[atual] = ordem_atual  # Numerar vértice encontrado
            ordem_atual += 1

        if atual == goal:
            return reconstruir_caminho(caminhos, start, goal), visitados, ordem_visita, ordem_map

        for vizinho in reversed(labirinto.vizinhos_validos(*atual)):
            if vizinho not in visitados:
                caminhos[vizinho] = atual
                pilha.append(vizinho)

    # Retornar valores vazios caso o objetivo não seja encontrado
    return [], visitados, ordem_visita, ordem_map
