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
    visitados = set([start])
    caminhos = {start: None}
    ordem_visita = []

    while fila:
        atual = fila.popleft()
        ordem_visita.append(atual)

        if atual == goal:
            return reconstruir_caminho(caminhos, start, goal), visitados, ordem_visita

        for vizinho in labirinto.vizinhos_validos(*atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                caminhos[vizinho] = atual
                fila.append(vizinho)

    return [], visitados, ordem_visita

def busca_profundidade(labirinto, start, goal):
    pilha = [start]
    visitados = set()
    caminhos = {start: None}
    ordem_visita = []

    while pilha:
        atual = pilha.pop()

        if atual not in visitados:
            visitados.add(atual)
            ordem_visita.append(atual)

            if atual == goal:
                return reconstruir_caminho(caminhos, start, goal), visitados, ordem_visita

            for vizinho in reversed(labirinto.vizinhos_validos(*atual)):
                if vizinho not in visitados:
                    caminhos[vizinho] = atual
                    pilha.append(vizinho)

    return [], visitados, ordem_visita
