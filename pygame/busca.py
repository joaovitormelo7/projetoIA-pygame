import heapq
from collections import deque


def busca_largura(labirinto, start, goal):
    if not labirinto.espaco_livre(*start) or not labirinto.espaco_livre(*goal):
        print("Posições inicial ou objetivo inválidas.")
        return []

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
    if not labirinto.espaco_livre(*start) or not labirinto.espaco_livre(*goal):
        print("Posições inicial ou objetivo inválidas.")
        return []

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

def busca_gulosa(labirinto, start, goal):
    if not labirinto.espaco_livre(*start) or not labirinto.espaco_livre(*goal):
        print("Posições inicial ou objetivo inválidas.")
        return []

    # Função de heurística (distância de Manhattan)
    def heuristica(posicao):
        x1, y1 = posicao
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)

    # Fila de prioridade para a busca gulosa
    fila_prioridade = [(heuristica(start), start)]
    visitados = set()  # Inicializa o conjunto de visitados
    caminhos = {start: None}  # Para reconstruir o caminho

    while fila_prioridade:
        _, (x, y) = heapq.heappop(fila_prioridade)

        # Verifica se o objetivo foi alcançado
        if (x, y) == goal:
            return reconstruir_caminho(caminhos, start, goal)

        # Marca a célula como visitada
        if (x, y) not in visitados:
            visitados.add((x, y))

            # Explora os vizinhos válidos
            for nx, ny in labirinto.vizinhos_validos(x, y):
                if (nx, ny) not in visitados:
                    heapq.heappush(fila_prioridade, (heuristica((nx, ny)), (nx, ny)))
                    caminhos[(nx, ny)] = (x, y)

    # Se nenhum caminho foi encontrado
    return []


def reconstruir_caminho(caminhos, start, goal):
    caminho = []
    atual = goal
    while atual is not None:
        caminho.append(atual)
        atual = caminhos[atual]
    return caminho[::-1]  # Inverte o caminho para começar do início
