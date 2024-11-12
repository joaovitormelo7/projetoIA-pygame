from collections import deque

#Usando busca em largura
def buscaLargura(labirinto, start, goal):
    fila = deque([start])
    visitado = set()
    visitado.add(start)

    #Encontrar o objetivo
    while fila:
        x, y = fila.popleft()
        if(x, y) == goal:
            return True
        for nx, ny in labirinto.vizinhos_validos(x, y):
            if(nx, ny) not in visitado:
                visitado.add((nx,ny))
                fila.append((nx, ny))
            return False

#Usando busca em profundidade
def buscaProfundidade(labirinto, start, goal):
    pilha = [(start)]
    visitado = set()
    while pilha:
        x, y = pilha.pop()
        if (x, y) == goal:
            return True 
        visitado.add((x, y))
        for nx, ny in labirinto.vizinhos_validos(x, y):
            if (nx, ny) not in visitado:
                pilha.append((nx, ny))
            return False
        
#Usando busca heurística A* com distância Manhattan

        