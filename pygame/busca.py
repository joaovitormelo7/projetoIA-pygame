import heapq
from collections import deque

# Usando busca em largura
def buscaLargura(labirinto, start, goal):
    fila = deque([start])
    visitado = set()
    visitado.add(start)
    caminhos = {start: None}

    # Encontrar o objetivo
    while fila:
        x, y = fila.popleft()
        if (x, y) == goal:
            caminho = []
            while (x, y) is not None:
                caminho.append((x,y))
                x, y = caminhos[(x, y)]
                return caminho[::-1]
            
        for nx, ny in labirinto.vizinhos_validos(x, y):
            if (nx, ny) not in visitado:
                visitado.add((nx, ny))
                fila.append((nx, ny))
                caminhos[(nx, ny)] = (x, y)
    return []

# Usando busca em profundidade
def buscaProfundidade(labirinto, start, goal):
    pilha = [start]
    visitado = set()
    caminhos = {start: None}

    while pilha:
        x, y = pilha.pop()
        if (x, y) == goal:
            caminho = []
            while(x, y) is not None:
                caminho.append((x, y))
                x, y = caminhos[(x,y)]
                return caminho[::-1]
             
        visitado.add((x, y))
        for nx, ny in labirinto.vizinhos_validos(x, y):
            if (nx, ny) not in visitado:
                pilha.append((nx, ny))
                caminhos[(nx, ny)] = (x, y)
    return []