import heapq
from collections import deque

def busca_largura(labirinto, start, goal):
    fila = deque([start])
    visitados = set([start])
    caminhos = {start: None}

    while fila:
        x, y = fila.popleft()

        if (x, y) == goal:
            return reconstruir_caminho(caminhos, start, goal)

        # Mantém a ordem padrão para BFS
        for nx, ny in labirinto.vizinhos_validos(x, y):
            if (nx, ny) not in visitados:
                visitados.add((nx, ny))
                fila.append((nx, ny))
                caminhos[(nx, ny)] = (x, y)
    return []


def busca_profundidade(labirinto, start, goal):
    pilha = [start]
    visitados = set()
    caminhos = {start: None}

    while pilha:
        x, y = pilha.pop()

        if (x, y) == goal:
            return reconstruir_caminho(caminhos, start, goal)

        if (x, y) not in visitados:
            visitados.add((x, y))

            # Explora na ordem inversa para DFS
            for nx, ny in reversed(labirinto.vizinhos_validos(x, y)):
                if (nx, ny) not in visitados:
                    pilha.append((nx, ny))
                    caminhos[(nx, ny)] = (x, y)
    return []


def reconstruir_caminho(caminhos, start, goal):
    caminho = []
    atual = goal
    while atual is not None:
        caminho.append(atual)
        atual = caminhos[atual]
    return caminho[::-1]  # Inverte o caminho para começar do início
