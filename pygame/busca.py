from collections import deque
import heapq

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

def busca_a_estrela(labirinto, start, goal):
    def heuristica(atual, goal):
        return abs(atual[0] - goal[0]) + abs(atual[1] - goal[1]) # Distancia de Manhattan
    
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, start))
    visitados = set()
    caminhos = {start: None}
    custo_atual = {start: 0}
    ordem_visita = []

    while fila_prioridade:
        _, atual = heapq.heappop(fila_prioridade)
        ordem_visita.append(atual)

        if atual == goal:
            return reconstruir_caminho(caminhos, start, goal), visitados, ordem_visita
        
        visitados.add(atual)

        for vizinho in labirinto.vizinhos_validos(*atual):
            novo_custo = custo_atual[atual] + 1 # Custo do movimento

            if vizinho not in custo_atual or novo_custo < custo_atual[vizinho]:
                custo_atual[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, goal)
                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                caminhos[vizinho] = atual
                
    return [], visitados, ordem_visita